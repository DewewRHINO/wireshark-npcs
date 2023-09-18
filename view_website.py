import webbrowser
import sys

def view_website(website_url):
    try:
        webbrowser.open(website_url)
        print(f"Viewed website: {website_url}")
    except Exception as e:
        print(f"Website View Error: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python view_website.py WEBSITE_URL")
        sys.exit(1)

    website_url = sys.argv[1]

    view_website(website_url)
