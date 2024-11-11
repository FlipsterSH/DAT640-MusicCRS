from openai import OpenAI
from keys import get_api_keys



def get_chat_completion(instructions, specifications):
    priv = get_api_keys()
    client = OpenAI(api_key=priv)
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": instructions
            },

            {
                "role": "user",
                "content": specifications
            }
        ]
    )

    print(f"AI completion: {completion.choices[0].message.content}")
    return completion.choices[0].message.content




def get_chat_completion1(userinput):
    instructions = """
    You are an assistant trying to help a user build a playlist by interpreting the users intentions though natural language. 
    These are the available commands for building the playlist:
    /add songname
    /remove songname
    /list
    /clear
    /add-specific song_title;artist;album_title

    These are the available questions you can write:
    When was album X released?
    How many Albums has X released?
    Which album features song X
    Command not found

    These are examples:
    This is the user input: Hello i want to add Tanssi vaan to the playlist
    This is what you should reply: /add Tanssi vaan

    This is the user input: Hello i want to remove Tanssi vaan from the playlist
    This is what you should reply: /remove Tanssi vaan 

    This is the user input: Hello i want to list all songs
    This is what you should reply: /list

    This is the user input: Hello i want to clear the playlist
    This is what you should reply: /clear

    This is the user input: Hi i want to add Love Story by Taylor Swift from the album Love Story
    This is what you should reply: /add-specific Love Story;Taylor Swift;Love Story

    This is the user input: Could you please tell me when the album Love Story was released?
    This is what you shold reply: When was album Love Story released?

    This is the user input: Hi, i want to know how many albums Taylor Swift has released
    This is what you should reply: How many albums has Taylor Swift released?

    This is the user input: In what album is the song Love Story featured?
    This is what you should reply: Which album features song Love Story

    If the userinput does not match any of the intended functions or questions, you should respond with command not found.
    """

    specifications = f"""
    When writing a command the command should not have a space between the / and the comand word. Ie. the command should be written as /add or /list
    This is the user input that you should interpret: {userinput}
    """


    priv = get_api_keys()
    client = OpenAI(api_key=priv)
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": instructions
            },

            {
                "role": "user",
                "content": specifications
            }
        ]
    )

    print(f"AI completion: {completion.choices[0].message.content}")

    return completion.choices[0].message.content



if __name__ == "__main__":
    instructions = """
    You are an assistant trying to interpret user intentions. 
    A user may add song to playlist by songname, remove song from playlist by song name, list out all the song in the playlist or clear the playlist.
    These are the available commands you can write:
    /add songname
    /remove songname
    /list
    /clear
    /add-specific song_title;artist;album_title
    When was album X released?
    How many Albums has X released?
    Which album features song X
    Command not found

    These are examples:
    This is the user input: Hello i want to add Tanssi vaan to the playlist
    This is what you should reply: /add Tanssi vaan

    This is the user input: Hello i want to remove Tanssi vaan from the playlist
    This is what you should reply: /remove Tanssi vaan 

    This is the user input: Hello i want to list all songs
    This is what you should reply: /list

    This is the user input: Hello i want to clear the playlist
    This is what you should reply: /clear

    This is the user input: Hi i want to add Love Story by Taylor Swift from the album Love Story
    This is what you should reply: /add-specific Love Story;Taylor Swift;Love Story

    This is the user input: Could you please tell me when the album Love Story was released?
    This is what you shold reply: When was album Love Story released?

    This is the user input: Hi, i want to know how many albums Taylor Swift has released
    This is what you should reply: How many albums has Taylor Swift released?

    This is the user input: In what album is the song Love Story featured?
    This is what you should reply: Which album features song Love Story?

    If the userinput does not match any of the intended functions or questions, you should respond with command not found.
    """

    specifications = f"""
    This is the user input: In which album is Shine Bright featured?
    """

    completion = get_chat_completion(instructions, specifications)
    print(completion)