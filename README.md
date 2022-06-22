# Language usage on Github
Discover which languages you utilise the most using the Github REST API


## Run
To find out the percentages,
```sh
python3 main.py
```
which will ask you for your github username,
```terminal
Enter your Github username: 
```
As well as a token.

This is optional; including a token allows private repositories to be included.
If you don't have one, simply enter to proceed.
A github personal token may be created at https://github.com/settings/tokens. 
```
Enter your Github token:
```
The script will then output a dictionary. 
```terminal
{'TeX': 41.81, 'Python': 21.64, 'C++': 8.5, 'Jupyter Notebook': 5.4, 'PureBasic': 4.99, 'HTML': 4.64, 'JavaScript': 3.42, 'HCL': 3.11, 'Shell': 2.98, 'EJS': 1.63, 'Ruby': 1.23, 'Dockerfile': 0.39, 'PHP': 0.26}
```

<br>

## Dependencies

- [requests](https://pypi.org/project/requests/); versions == any; requires.python>=3.7


<br>

## Resources

- https://docs.github.com/en/rest/guides/getting-started-with-the-rest-api
- https://docs.github.com/en/rest/guides/basics-of-authentication