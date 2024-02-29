from blessed import Terminal
import modules.audio_player


def render_attack_boxes(content: list[str], width_per_box: int, height_per_box: int, space_between_boxes: int = 5, auto_scale: bool = False) -> None:
    """DEPRACATED. Use render_box() instead. Renders attack boxes in a row with the one-line content given, as well as their widths, heights, and the space between them.
    If auto_scale is True, the box size will instead be automatically adjusted with width_per_box and height_per_box as the horizontal and vertical padding respectively."""


    lines: list[str] = ['' for _ in range(height_per_box)]

    if auto_scale:
        box_height: int = 0
        box_width: int = 0

        for box_content in content:
            lines: list[str] = box_content.split('\n')
            for line in lines:
                
                if len(line) + 2 + 2 * width_per_box > box_width:
                    box_width = len(line) + 2 + 2 * width_per_box

            if len(lines) + height_per_box * 2 + 2 > box_height:
                box_height = len(lines) + height_per_box * 2 + 2
                
        lines = ["" for _ in range(box_height)]

        height_per_box = box_height
        width_per_box = box_width
        print(f"{height_per_box}, {width_per_box}, {len(lines)}")

    for box_content in content:
        start_empty_row: int = 0
        end_empty_row: int = 0
        box_lines = box_content.split('\n')
        content_height: int = len(box_lines)

        # if auto_scale:
        #     box_height: int = 0
        #     box_width: int = 0

        #     for item in box_content:
        #         lines: list[str] = item.split()
        #         if len(lines) + height_per_box * 2 + 2 > box_height:
        #             box_height = len(lines) + height_per_box * 2 + 2
        #         for line in lines:
        #             if len(line) + 2 + 2 * width_per_box > box_width:
        #                 box_width = len(line) + 2 + 2 * width_per_box
            
            # height_per_box = box_height
            # width_per_box = box_width

        if content_height > height_per_box - 2:
            exit(f"Error: tried filling box of size {height_per_box} (inside {height_per_box - 2}) with {content_height} of content.")

        if (height_per_box - content_height) % 2 == 1:
            start_empty_row = (height_per_box - content_height - 3) //2
            end_empty_row = start_empty_row + 1

        else:
            start_empty_row = (height_per_box - content_height - 2) // 2
            end_empty_row = start_empty_row

        lines[0] += '╔' + '═' * (width_per_box - 2) + '╗' + ' ' * space_between_boxes

        for i in range(start_empty_row):
            lines[i + 1] += '║' + ' ' * (width_per_box - 2) + '║' + ' ' * space_between_boxes

        # if type(box_content) is str:
        #     start_empty_col: int = 0
        #     end_empty_col: int = 0

        #     if (len(box_content) + width_per_box) % 2 == 1:
        #         start_empty_col = (width_per_box - 2 - len(box_content) - 1) // 2
        #         end_empty_col = start_empty_col + 1

        #     else:
        #         start_empty_col = (width_per_box - 2 - len(box_content)) // 2
        #         end_empty_col = start_empty_col

        #     lines[start_empty_row + 1] += '║' + ' ' * start_empty_col + box_content + ' ' * end_empty_col + '║' + ' ' * space_between_boxes

        # else:
        for i, line in enumerate(box_lines):
            start_empty_col: int = 0
            end_empty_col: int = 0

            if (len(line) + width_per_box) % 2 == 1:
                start_empty_col = (width_per_box - 2 - len(line) - 1) // 2
                end_empty_col = start_empty_col + 1

            else:
                start_empty_col = (width_per_box - 2 - len(line)) // 2
                end_empty_col = start_empty_col

            lines[start_empty_row + 1 + i] += '║' + ' ' * start_empty_col + line + ' ' * end_empty_col + '║' + ' ' * space_between_boxes



        for i in range(end_empty_row):
            lines[start_empty_row + 1 + content_height + i] += '║' + ' ' * (width_per_box - 2) + '║' + ' ' * space_between_boxes


        lines[len(lines) - 1] += '╚' + '═' * (width_per_box - 2) + '╝' + ' ' * space_between_boxes

    for line in lines:
        print(line)


    # print(('╔' + '═' * (width_per_box - 2) + '╗' + ' ' * space_between_boxes) * len(content))
    # start_empty_row: int = 0
    # end_empty_row: int = 0

    # if height_per_box % 2 == 1:
    #     start_empty_row = (height_per_box - 3) // 2
    #     end_empty_row = start_empty_row

    # else:
    #     start_empty_row = (height_per_box - 2) // 2
    #     end_empty_row = start_empty_row - 1

    # for _ in range(start_empty_row):
    #     print(('║' + ' ' * (width_per_box - 2) + '║' + ' ' * space_between_boxes) * len(content))

    # for box_content in content:
    #     start_empty_col: int = 0
    #     end_empty_col: int = 0

    #     if (len(box_content) + width_per_box) % 2 == 1:
    #         start_empty_col = (width_per_box - 2 - len(box_content) - 1) // 2
    #         end_empty_col = start_empty_col + 1

    #     else:
    #         start_empty_col = (width_per_box - 2 - len(box_content)) // 2
    #         end_empty_col = start_empty_col

    #     print('║' + ' ' * start_empty_col + box_content + ' ' * end_empty_col + '║' + ' ' * space_between_boxes, end = "")  # noqa: E251

    # print("")

    # for _ in range(end_empty_row):
    #     print(('║' + ' ' * (width_per_box - 2) + '║' + ' ' * space_between_boxes) * len(content))

    # print(('╚' + '═' * (width_per_box - 2) + '╝' + ' ' * space_between_boxes) * len(content))




def render_box(terminal: Terminal, content: str, x: int, y: int, width: int, height: int, auto_scale: bool = False, center_content: bool = False) -> None:
    """Renders a box with content at position [x, y]. Width and height is the total width and height of the box, if auto_scale is true then this is changed to the horizontal and vertical padding around the text."""

    if auto_scale:
        content_lines: list[str] = content.split('\n')
        final_width: int = 0

        for line in content_lines:
            if len(line) + 2 * width + 2 > final_width:
                final_width = len(line) + 2 * width + 2

        if not center_content:
            final_width -= width
            height = len(content_lines) + height + 2

        else:
            height = len(content_lines) + 2 * height + 2
        width = final_width
        
        

    lines: list[str] = ["" for _ in range(height)]
    start_empty_row: int = 0
    end_empty_row: int = 0
    box_lines: list[str] = [] # = content.split('\n')

    if not center_content:
        # box_lines = content.split('\n')

        for i, content_line in enumerate(content.split('\n')):
            if not auto_scale and len(content_line) - 2 > width:
                content_line = content_line[0:width - 2]  # noqa: PLW2901

                if i > height - 2:
                    break

            box_lines.append(content_line)
            

        end_empty_row = height - len(box_lines) - 2

    else:
        for i, content_line in enumerate(content.split('\n')):

            if len(content_line) - 2 > width:
                content_line = content_line[0:width - 2]  # noqa: PLW2901

            if i > height - 2:
                break

            box_lines.append(content_line)
            
        if (height - len(box_lines)) % 2 == 1:
            start_empty_row = (height - len(box_lines) - 3) //2
            end_empty_row = start_empty_row + 1

        else:
            start_empty_row = (height - len(box_lines) - 2) // 2
            end_empty_row = start_empty_row

    lines[0] += '╔' + '═' * (width - 2) + '╗'

    for i in range(start_empty_row):
        lines[i + 1] += '║' + ' ' * (width - 2) + '║'

    for i, line in enumerate(box_lines):
        start_empty_col: int = 0
        end_empty_col: int = 0

        if center_content:
            if (len(line) + width) % 2 == 1:
                start_empty_col = (width - 2 - len(line) - 1) // 2
                end_empty_col = start_empty_col + 1

            else:
                start_empty_col = (width - 2 - len(line)) // 2
                end_empty_col = start_empty_col

        else:
            end_empty_col = width - 2 - len(line)

        lines[start_empty_row + 1 + i] += '║' + ' ' * start_empty_col + line + ' ' * end_empty_col + '║'



    for i in range(end_empty_row):
        lines[start_empty_row + 1 + len(box_lines) + i] += '║' + ' ' * (width - 2) + '║'

    lines[len(lines) - 1] += '╚' + '═' * (width - 2) + '╝'

    for i, line in enumerate(lines):
        print(terminal.move_xy(x, y + i) + line)


def check_spelling(spelling_to_check: str, reference_string: str, allowed_errors: int = 0, case_sensitive: bool = True) -> bool:
    """Checks a given string against a reference string for spelling mistakes. """

    string_pos: int = 0
    reference_string_pos: int = 0
    errors: int = 0
    
    if not case_sensitive:
        spelling_to_check = spelling_to_check.lower()
        reference_string = reference_string.lower()

    while True:
        if string_pos >= len(spelling_to_check):
            final_errors: int = len(reference_string) - reference_string_pos - 1

            if final_errors > 0:
                errors += final_errors

            if errors > allowed_errors:
                return False
            
            return True

        if reference_string_pos >= len(reference_string):
            final_errors: int = len(spelling_to_check) - string_pos - 1

            if final_errors > 0:
                errors += final_errors

            if errors > allowed_errors:
                return False

            return True

        if errors > allowed_errors:
            return False
        
        # Check if character correct
        if spelling_to_check[string_pos] == reference_string[reference_string_pos]:
            string_pos += 1
            reference_string_pos += 1
            continue

        # Check for swapped characters
        if len(reference_string) > reference_string_pos + 1 and len(spelling_to_check) > string_pos + 1 and reference_string[reference_string_pos + 1] == spelling_to_check[string_pos] and reference_string[reference_string_pos] == spelling_to_check[string_pos + 1]:
            errors += 1
            string_pos += 2
            reference_string_pos += 2
            continue

        # Check for extra character
        if len(spelling_to_check) > string_pos + 1 and spelling_to_check[string_pos + 1] == reference_string[reference_string_pos]:
            errors += 1
            string_pos += 2
            reference_string_pos += 1
            continue

        # Check for removed character
        if len(reference_string) > reference_string_pos + 1 and spelling_to_check[string_pos] == reference_string[reference_string_pos + 1]:
            errors += 1
            reference_string_pos += 1
            continue

        #Wrong character
        errors += 1
        reference_string_pos += 1
        string_pos += 1




        

    
    
    






if __name__ == "__main__":
    terminal: Terminal = Terminal()
    render_attack_boxes(["12345", "12", "123456789\n1234\n1234567\n1\n\n1234567891234567", "123456789123"], 4, 3, 8, True)
    # p = AudioSegment.from_mp3("file.mp3")
    # play(p)
    # player: vlc.MediaPlayer = vlc.MediaPlayer("file.mp3")
    # player.play()
    # modules.audio_player.play_music("file.mp3")
    render_box(terminal, "qfwrre\neeeeee\n12345678", 10, 7, 2, 2, True)
    render_box(terminal, "108e2r929rd8wf989", 30, 15, 6, 1, True)
    render_box(terminal, "108e2r929rd8wf989", 60, 8, 0, 0, True)
    render_box(terminal, "yooooooaaaaaaauuuuuuuiiiiiiieeeeeee\nApples", 30, 30, 15, 6)
    render_box(terminal, "test test test\nuuu test test", 30, 40, 2, 2, True, False)
    print(check_spelling("word", "word")) # True
    print(check_spelling("word", "wrod")) # False
    print(check_spelling("word", "wrod", 1)) # True
    print("_-_-_-_-_-_-_-_")
    print(check_spelling("word", "wrd")) # False
    print(check_spelling("word", "wrd", 1)) # True
    print(check_spelling("word", "worrd")) # False
    print(check_spelling("word", "worrd", 1)) # True
    print("----------------")
    print(check_spelling("yeopeeyrpeop", "yepeeyrpeeop")) # False
    print(check_spelling("yeopeeyrpeop", "yepeeyrpeeop", 1)) # False
    print(check_spelling("yeopeeyrpeop", "yepeeyrpeeop", 2)) # True
    print("_-_-_-_-_-_-_-_")
    print(check_spelling("yeopeeyRpeop", "yepeeyrpeeop", 2, False)) # True
    print(check_spelling("yeopeeyRpeop", "yepeeyrpeeop", 2)) # False
    print(check_spelling("yeopeeyRpeop", "yepeeyrpeeop", 3)) # True
    yooo: str = input()
