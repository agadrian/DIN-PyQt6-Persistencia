from fpdf import FPDF
from PyQt6.QtWidgets import QTableWidget, QApplication
import sys
from datetime import datetime
import os
import textwrap

class PDFGenerator(FPDF):
    def __init__(self, orientation='P', unit='mm', format='A4'):
        super().__init__(orientation, unit, format)
        self.set_auto_page_break(auto=True, margin=15)
        self.add_page()
        self.set_font('Arial', '', 12)
        
    def header(self):
        # Logo
        self.image('ui/img/logoLogin.png', 10, 8, 20)  # Ajusta la ruta y tamaño según tu logo
        # Cabecera
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, 'Nombre de la Empresa', 0, 1, 'C')
        self.ln(15)
        
    def footer(self):
        # Pie de página
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')
    
    def add_title(self, title):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, title, 0, 1, 'C')
        self.ln(10)




    def generate_table_from_qtwidget(self, table_widget, title="Reporte de Datos"):
        """
        Genera un PDF con una tabla a partir de un QTableWidget
        
        Args:
            table_widget: QTableWidget con los datos
            title: Título del reporte
        """
        self.add_title(title)
        
        # Obtener datos de la tabla
        rows = table_widget.rowCount()
        cols = table_widget.columnCount()-1
        
        # Obtener encabezados
        headers = []
        for col in range(cols):
            header_item = table_widget.horizontalHeaderItem(col)
            header_text = header_item.text() if header_item else f"Columna {col+1}"
            headers.append(header_text)
        
        # Inicializar anchuras basadas en los encabezados
        col_widths = [self.get_string_width(header) + 5 for header in headers]
        
        # Escanear todas las celdas para encontrar el contenido más largo en cada columna
        for col in range(cols):
            max_width = col_widths[col]
            
            for row in range(rows):
                item = table_widget.item(row, col)
                if item:
                    text = item.text()
                    text_width = self.get_string_width(text) + 5  # Añadir margen
                    
                    # Limitar el ancho máximo para evitar columnas extremadamente anchas
                    # Ajusta el valor 60 según tus necesidades
                    max_width = min(max(max_width, text_width), 60)
            
            col_widths[col] = max_width
        
        # Verificar que la suma de anchos no exceda el ancho de página
        page_width = self.w - 20  # Margen de 10mm a cada lado
        total_width = sum(col_widths)
        
        # Si excede, ajustar proporcionalmente
        if total_width > page_width:
            ratio = page_width / total_width
            col_widths = [width * ratio for width in col_widths]
        
        # Dibujar encabezados
        self.set_font('Arial', 'B', 10)
        self.set_fill_color(200, 230, 200)  # Verde claro
        
        for i, header in enumerate(headers):
            self.cell(col_widths[i], 10, header, 1, 0, 'C', 1)
        self.ln()
        
        # Dibujar datos
        self.set_font('Arial', '', 10)
        self.set_fill_color(255, 255, 255)  # Blanco
        
        # Calcular cuántos caracteres caben en cada columna (aproximadamente)
        font_size = 10  # Tamaño de fuente en puntos
        avg_char_width = self.get_string_width('a')  # Ancho promedio de un carácter
        
        for row in range(rows):
            row_data = []
            max_lines = 1
            
            # Preparar los datos de la fila
            for col in range(cols):
                item = table_widget.item(row, col)
                text = item.text() if item else ""
                
                # Calcular cuántos caracteres caben en la columna
                chars_per_line = int((col_widths[col] - 4) / avg_char_width)
                chars_per_line = max(chars_per_line, 1)  # Al menos 1 carácter
                
                # Dividir el texto en líneas
                if len(text) > chars_per_line:
                    # Usar textwrap para dividir el texto en líneas
                    lines = textwrap.wrap(text, width=chars_per_line)
                else:
                    lines = [text]
                
                row_data.append(lines)
                max_lines = max(max_lines, len(lines))
            
            # Calcular la altura para cada línea (mínimo 6mm)
            line_height = max(6, font_size / 2 + 2)
            
            # Calcular la altura total de la celda
            cell_height = line_height * max_lines
            
            # Dibujar la fila con múltiples líneas
            y_pos = self.get_y()
            
            # Dibujar cada celda de la fila
            for col in range(cols):
                x_pos = self.get_x()
                
                # Dibujar el borde de la celda
                self.rect(x_pos, y_pos, col_widths[col], cell_height)
                
                # Calcular el espacio vertical para centrar el contenido
                content_lines = row_data[col]
                content_height = len(content_lines) * line_height
                
                # Calcular el padding vertical para centrar
                v_padding = (cell_height - content_height) / 2
                
                # Dibujar cada línea de texto centrada verticalmente
                for i, line in enumerate(content_lines):
                    # Calcular la posición Y para centrar verticalmente
                    line_y = y_pos + v_padding + (i * line_height)
                    
                    self.set_xy(x_pos, line_y)
                    self.cell(col_widths[col], line_height, line, 0, 0, 'C')
                
                # Mover a la siguiente columna
                self.set_x(x_pos + col_widths[col])
            
            # Mover a la siguiente fila
            self.set_y(y_pos + cell_height)


    
    def save(self, filename):

        # Crear la carpeta 'Informes' si no existe
        informes_dir = "Informes"
        if not os.path.exists(informes_dir):
            os.makedirs(informes_dir)
        
        # Obtener el nombre del archivo sin la ruta
        base_filename = os.path.basename(filename)
        
        # Obtener la fecha y hora actual en formato dd_mm_yyyy_hh_mm_ss
        timestamp = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
        
        
        # Crear el nuevo nombre con el timestamp
        name, ext = os.path.splitext(base_filename)
        new_filename = f"{name}_{timestamp}{ext}"
        
        # Ruta completa para guardar los pdf
        full_path = os.path.join(informes_dir, new_filename)
        
        # Guardar el PDF con el nuevo nombre en la carpeta 'Informes'
        self.output(full_path)
        
        return full_path

    
