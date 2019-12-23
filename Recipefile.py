#!/usr/bin/python3
import os
import shutil

def remove(spirit):
    shutil.rmtree(spirit.git.working_dir)


def pull(spirit, progress):
    repo = spirit.git
    remote = repo.remote(name="origin")
    remote.pull(progress=progress)
    print("Pulled from: " + spirit.github_repo.full_name)
