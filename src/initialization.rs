use std::env;
use std::fs;
use std::path::Path;

pub fn initializtor() {
    let current_dir = env::current_dir().expect("Failed to get current directory");
    let git_dir = current_dir.join(".git");

    if git_dir.exists() {
        println!("A .git directory already exists in this location.");
        return;
    }

    fs::create_dir(&git_dir).expect("Failed to create .git directory");

    fs::create_dir(git_dir.join("branches")).expect("Failed to create branches directory");
    fs::create_dir(git_dir.join("hooks")).expect("Failed to create hooks directory");
    fs::create_dir(git_dir.join("info")).expect("Failed to create info directory");
    fs::create_dir(git_dir.join("objects")).expect("Failed to create objects directory");
    fs::create_dir(git_dir.join("refs")).expect("Failed to create refs directory");
    fs::create_dir(git_dir.join("refs/heads")).expect("Failed to create refs/heads directory");

    fs::write(git_dir.join("HEAD"), "ref: refs/heads/master").expect("Failed to create HEAD file");

    println!("Initialized empty Git repository in {}", git_dir.display());
}
