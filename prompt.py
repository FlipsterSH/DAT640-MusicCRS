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

    return completion.choices[0].message.content




def get_chat_completion1(userinput):
    instructions = """
        You are an assistant trying to interpret user intentions.
        A user may add song to playlist by songname, remove song from playlist by song name, list out all the song in the playlist or clear the playlist.
        These are the available commands you can write:
        /add songname
        /remove songname
        /list
        /clear

        These are examples:
        This is the user input: Hello i want to add Tanssi vaan to the playlist
        This is what you should reply: /add Tanssi vaan

        This is the user input: Hello i want to remove Tanssi vaan from the playlist
        This is what you should reply: /remove Tanssi vaan

        This is the user input: Hello i want to list all songs
        This is what you should reply: /list

        This is the user input: Hello i want to clear the playlist
        This is what you should reply: /clear
        """

    specifications = f"""
    This is the user input: {userinput}
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

    These are examples:
    This is the user input: Hello i want to add Tanssi vaan to the playlist
    This is what you should reply: /add Tanssi vaan

    This is the user input: Hello i want to remove Tanssi vaan from the playlist
    This is what you should reply: /remove Tanssi vaan 

    This is the user input: Hello i want to list all songs
    This is what you should reply: /list

    This is the user input: Hello i want to clear the playlist
    This is what you should reply: /clear
    """

    specifications = """
    This is the user input: Heyy, can you add Love Story to the playlist?
    """

    completion = get_chat_completion(instructions, specifications)
    print(completion)