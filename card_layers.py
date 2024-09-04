import cv2
import numpy as np

""" Card dict example:
{
    "name": "Forest Guardian",
    "family": "forest_humanoids",
    "type": "character",
    "mana": 1,
    "HP": 2,
    "defence": 1,
    "attack": 1,
    "prompt": "A half-elf warrior with green skin, dressed in a leafy cloak and holding a staff made from twisted vines. The background should feature a serene forest with towering trees, sunlight filtering through the leaves. The Guardian's eyes should glow softly like embers."
},
{
    "name": "Forest Shield",
    "family": "forest_humanoids",
    "type": "object",
    "mana": 1,
    "effect": "Grant this card +1 defence until end of turn",
    "prompt": "A glowing, translucent shield with intricate leaf patterns. It should be surrounded by a halo of soft light and have a gentle, pulsing quality to it. The background could feature a misty forest clearing at dawn or dusk."
},

"""


def add_layers_to_card(card_img_path, card_dict):
    image = cv2.imread(card_img_path)
    # Check if the image was loaded successfully
    if image is None:
        raise FileNotFoundError(f"Image not found at path: {card_img_path}")

    #region CARD NAME ----------------------
    # Define the color for the golden bar (in BGR format)
    golden_color = (3, 186, 252)
    golden_color2 = (2, 132, 219)
    green_color = (97, 196, 26)
    green_color2 = (33, 74, 4)
    brown_color = (0, 71, 153)
    brown_color2 = (1, 35, 75)
    grey_color = (74, 64, 62)
    grey_color2 = (41, 34, 33)
    black_color = (0, 0, 0)

    if card_dict['family'] == 'Forest Humanoids': 
        bar_color = green_color
        barborder_color = green_color2
    elif card_dict['family'] == 'Animals':
        bar_color = brown_color
        barborder_color = brown_color2
    elif card_dict['family'] == 'Phantoms':
        bar_color = grey_color
        barborder_color = grey_color2

    # Define margins
    top_margin = 325
    side_margin = 10
    bar_height = 20
    bar_width = image.shape[1] - 2 * side_margin

    image[top_margin:top_margin + bar_height, side_margin:side_margin + bar_width] = bar_color
    # Draw a border
    cv2.rectangle(image, (side_margin, top_margin), (side_margin + bar_width, top_margin + bar_height), barborder_color, 2)

    # Add text to label the golden bar
    # font = cv2.FONT_HERSHEY_COMPLEX
    font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
    font_scale = 0.5  # Reduced font size
    card_name = card_dict['name']
    (text_width, text_height), baseline = cv2.getTextSize(card_name, font, font_scale, 1)
    text_x = side_margin + (bar_width - text_width) // 2
    text_y = top_margin + (bar_height + text_height) // 2 # + baseline

    cv2.putText(image, card_name, (text_x, text_y), font, font_scale, black_color, 1, cv2.LINE_AA)
    # endregion

    #region MANA Add a blue circle with the number 5 on the top left corner
    circle_center = (15, 15)
    circle_radius = 15
    circle_color = (214, 167, 11)  # Blue color in BGR format
    circle_thickness = -1  # Fill the circle

    cv2.circle(image, circle_center, circle_radius, circle_color, circle_thickness)

    mana_cost = str(card_dict['mana'])
    text_org = (8, 22)
    font_scale = 0.7
    text_color = (255, 255, 255)  # White color in BGR format
    text_thickness = 2

    cv2.putText(image, mana_cost, text_org, cv2.FONT_HERSHEY_SIMPLEX, font_scale, text_color, text_thickness, cv2.LINE_AA)
    # endregion

    #region HP / att / deffence
    if card_dict['type'] == 'character':
        text = f'{card_dict["HP"]} HP      {card_dict["attack"]} Att      {card_dict["defence"]} Def'
        font_scale = 0.5
        font = cv2.FONT_HERSHEY_SIMPLEX
        text_thickness = 1
    elif card_dict['type'] == 'object':
        text = f'{card_dict["effect"]}'
        font_scale = 0.4
        font = cv2.FONT_HERSHEY_SIMPLEX
        text_thickness = 1 
    cv2.putText(image, text, (side_margin, top_margin-5), font, font_scale, text_color, text_thickness, cv2.LINE_AA)
    # endregion
    
    # Save the image
    cv2.imwrite(f'{card_img_path[:-4]+ "_layered.png"}', image)