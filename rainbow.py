import weechat

weechat.register("rainbow", "Luke Moll", "1.0", "BSD-3-clause", "Makes rainbow-colored messages!", "", "")

rainbow_colors = [x for x in range(52, 64)]

def rainbow_text(data, buffer, args):
    formatted = ""
    color_index = 0
    for c in args:
        formatted += "\x03{}{}".format(rainbow_colors[color_index], c)
        color_index = (color_index + 1) % len(rainbow_colors)
    weechat.command(buffer, "{}\x0F".format(formatted))
    return weechat.WEECHAT_RC_OK

weechat.hook_command("rainbow", "Sends a message in rainbow colors!", "[text]", "text to send", "", "rainbow_text", "")