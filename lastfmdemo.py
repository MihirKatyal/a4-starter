from LastFM import LastFM

def main():
    user = "YOUR_LASTFM_USERNAME"  # Replace this with your LastFM username
    api_key = "43effd57c3bbcfc8d88897c50b1cb0cf"  # Use your actual API key here

    last_fm = LastFM(user)
    last_fm.set_apikey(api_key)
    try:
        last_fm.load_top_tracks()
        last_fm.print_top_tracks()
    except ConnectionError as e:
        print(f"Error: {str(e)}")
    except ValueError as e:
        print(f"Error: {str(e)}")

if __name__ == '__main__':
    main()