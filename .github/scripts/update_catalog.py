from github import Github
import yaml
import sys

catalog_url = "jungtop/sample_catalog"
#catalog_url = "jungtop/sample_catalog"

token = sys.argv[1]
g = Github(token)


def get_catalog(g):
    try:
        repo = g.get_repo(catalog_url)
        contents = repo.get_contents(f"./demo.csv")
        catalog = yaml.safe_load(contents.decoded_content.decode())
        return catalog
    except:
        print('Repo Not Found')


def update_catalog():
    commit_msg = "updated catalog"
    catalog = get_catalog(g)
    updated_catalog =catalog+"new content"+"\n"
    update_repo(g,commit_msg,updated_catalog)



def update_repo(g,commit_msg,updated_catalog):
    try:
        repo = g.get_repo(catalog_url)
        contents = repo.get_contents(f"./demo.csv",ref="main")
        repo.update_file(contents.path, commit_msg, updated_catalog, sha=contents.sha, branch="main")
    except Exception as e:
        print(e) 
    
if __name__ == "__main__":
    update_catalog()

