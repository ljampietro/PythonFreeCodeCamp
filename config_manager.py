test_settings = {
    'theme': 'light',
    'dummy': 'set',
    'dummy2': 'set2',
    'dummy3': 3
}


def add_setting(setting, pair):
    # unpacks tuple
    key, value = pair
    # converts to lower if string
    key_lower = str(key).lower()
    value_lower = str(value).lower() if isinstance(value, str) else value
    # check if key exists
    if key_lower in setting:
        return f"Setting '{key_lower}' already exists! Cannot add a new setting with this name."
    # add new setting
    setting[key_lower] = value_lower
    return f"Setting '{key_lower}' added with value '{value_lower}' successfully!"


def update_setting(setting, pair):
    # unpacks tuple
    key, value = pair
    # converts to lower if string
    key_lower = str(key).lower()
    value_lower = str(value).lower() if isinstance(value, str) else value
    # check if key exists and updates
    if key_lower in setting:
        setting[key_lower] = value_lower
        return f"Setting '{key_lower}' updated to '{value_lower}' successfully!"
    else:
        return f"Setting '{key_lower}' does not exist! Cannot update a non-existing setting."


def delete_setting(dictionary, key):
    key_lower = str(key).lower()
    if key_lower in dictionary:
        del dictionary[key_lower]
        return f"Setting '{key_lower}' deleted successfully!"
    return 'Setting not found!'


def view_settings(setting):
    if not setting:
        return f"No settings available."
    else:
        # Adicionamos \n aqui para pular a linha após o título
        output = ("Current User Settings:""\n")

        for key, value in setting.items():
            # Adicionamos \n aqui para pular a linha após cada configuração
            sett = f"{key.capitalize()}: {value}" + "\n"
            output += sett
        return output