import requests

class Github:
    def __init__(self, username, token):
        self.username = username
        self.has_token = True if token else False
        self.token = ''
        self.languages_usage = self.calc_percent_per_lang()


    def get_user_info(self):
        headers = {'Authorization': 'token ' + self.token}
        url = 'https://api.github.com/users/' + self.username
        response = requests.get(url, headers=headers) if self.has_token else requests.get(url)
        return response.json()

    def get_repos(self):
        headers = {'Authorization': 'token ' + self.token}
        url = f'https://api.github.com/search/repositories?q=user:{self.username}'
        response = requests.get(url , headers=headers) if self.has_token else requests.get(url)
        return response.json()['items']

    def get_repo_names(self):
        return [repo['name'] for repo in self.get_repos()]

    def get_repo_language(self, repo_name):
        headers = {'Authorization': 'token ' + self.token}
        url = 'https://api.github.com/repos/' + self.username + '/' + repo_name + '/languages'
        response = requests.get(url, headers=headers) if self.has_token else requests.get(url)
        return response.json()

    def calculate_repo_language(self):
        dict_of_languages = {}
        for repo_name in self.get_repo_names():
            languages = self.get_repo_language(repo_name)

            for language, characters in languages.items():
                if language in dict_of_languages:
                    dict_of_languages[language] += characters
                else:
                    dict_of_languages[language] = characters
        
        return dict_of_languages

    def calc_percent_per_lang(self):
        dict_of_languages = self.calculate_repo_language()
        total_characters = sum(dict_of_languages.values())
        dict_of_languages_percent = {}

        for language, characters in dict_of_languages.items():
            # calclate percentage of each language to 2 decimal places
            dict_of_languages_percent[language] = round(characters / total_characters * 100, 2)

        # order the languages by percentage as a dictionary
        ordered_dict_of_languages_percent = {k: v for k, v in sorted(dict_of_languages_percent.items(), key=lambda item: item[1], reverse=True)}
        return ordered_dict_of_languages_percent


if __name__ == '__main__':
    # ask user for github username
    username = input("Enter your Github username: ")
    token = input("Enter your Github token: ") or None

    github_user = Github(username, token)
    print(github_user.languages_usage)
