from github import Github
import sys
try:
  g = Github(sys.argv[1])
  for repo in g.get_user().get_repos():
    print("!git clone https://"+sys.argv[1]+":x-oauth-basic@github.com/"+sys.argv[2]+"/"+repo.name+".git")
except IndexError:
     print("Usage: ./"+sys.argv[0]+" <Personal_Token> <Username>")
