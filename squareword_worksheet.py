import reportlab.pdfgen.canvas
from reportlab.lib.units import cm

CELL = 2 * cm
GAME_SQUARE = 5 * CELL
PADDING = 2 * CELL
GAME_COLS = 4
GAME_ROWS = 6

def draw_game_square(canvas, top_left):
    for x in range(0, 6):
        x_offset = top_left[0] + x * CELL
        y_offset = top_left[1]
        canvas.line(x_offset, y_offset, x_offset, y_offset + GAME_SQUARE)
        print(f"     drawing vertical line from ({x_offset},{y_offset}) to ({x_offset, y_offset + GAME_SQUARE})")
    for y in range(0, 6):
        x_offset = top_left[0]
        y_offset = top_left[1] + y * CELL
        canvas.line(x_offset, y_offset, x_offset + GAME_SQUARE, y_offset)
        print(f"     drawing horizontal line from ({x_offset},{y_offset}) to ({x_offset + GAME_SQUARE, y_offset})")


def generate_grid_paper(filename, width, height):
    top_left = (0,0)
    c = reportlab.pdfgen.canvas.Canvas(filename)

    # Set page size
    c.setPageSize((width, height))

    # Draw grid lines
    for y in range(0, GAME_ROWS):
        for x in range(0, GAME_COLS):
            print(f"drawing game square at {x}, {y}")
            draw_game_square(c, top_left)
            top_left = (top_left[0] + GAME_SQUARE + PADDING, top_left[1]) 
        top_left = (0, top_left[1] + GAME_SQUARE + PADDING) 


    # for x in range(0, int(width * inch), int(grid_size * inch)):
    #     c.line(x, 0, x, height * inch)
    # for y in range(0, int(height * inch), int(grid_size * inch)):
    #     c.line(0, y, width * inch, y)

    c.save()

if __name__ == '__main__':
    PAGE_WIDTH = GAME_SQUARE * GAME_COLS + (GAME_COLS - 1) * PADDING
    PAGE_HEIGHT = GAME_SQUARE * GAME_ROWS + (GAME_ROWS - 1) * PADDING
    generate_grid_paper('grid.pdf', PAGE_WIDTH, PAGE_HEIGHT)
    