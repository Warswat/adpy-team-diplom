import requests

def get_access_token(app_id, scope, redirect_uri):
    print(f"Open the following URL in a web browser and authorize the app:\n")
    print(f"https://oauth.vk.com/authorize?client_id={app_id}&scope={scope}&redirect_uri={redirect_uri}&response_type=token&revoke=1&v=5.199")
    access_token = input("Enter the access token from the redirected URL: ")
    return access_token

def like_post(access_token,ower_id, post_id):
    like_url = f"https://api.vk.com/method/likes.add?type=photo&owner_id={ower_id}&item_id={post_id}&access_token={access_token}&v=5.199"
    response = requests.get(like_url)
    data = response.json()
    if 'response' in data:
        print("Post liked successfully")
    else:
        if 'error' in data:
            error_code = data['error']['error_code']
            error_msg = data['error']['error_msg']
            print(f"Failed to like the post. Error code: {error_code}, Error message: {error_msg}")
        else:
            print("Failed to like the post. Unknown error")

if __name__ == "__main__":
    app_id = '51851383'  # Replace with your VK app ID
    scope = 'photos,wall'  # Replace with the scopes you need
    redirect_uri = 'https://oauth.vk.com/blank.html'  # Replace with your redirect URI

    post_id = '395355677'  # Replace with the ID of the post you want to like
    ower_id = '50765384'  # Replace with the ID of the owner of the post
    access_token = get_access_token(app_id, scope, redirect_uri)
    like_post(access_token, ower_id, post_id)