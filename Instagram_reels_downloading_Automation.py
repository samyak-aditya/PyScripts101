import instaloader
import time

def download_instagram_reels(profile_name):
    # Create an instance of Instaloader
    L = instaloader.Instaloader()

    # Login to your Instagram account (if needed)
    # L.login(USERNAME, PASSWORD)

    # Load the profile
    profile = instaloader.Profile.from_username(L.context, profile_name)

    # Iterate over the posts in the profile and download reels
    for post in profile.get_posts():
        if post.is_video and post.typename == 'GraphVideo':
            print(f"Downloading reel: {post.url}")
            L.download_post(post, target=f"{profile.username}_reels")
            print("Waiting for 1 minute before downloading the next reel...")
            time.sleep(60)  # Delay for 1 minute

if __name__ == "__main__":
    instagram_profile = input("Enter the Instagram profile name: ")
    download_instagram_reels(instagram_profile)
