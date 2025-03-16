use std::fs;
use std::io::{self, Write};
use std::path::Path;

pub fn init_repo(path: &str) -> io::Result<()> {
    let git_dir = Path::new(path).join(".git");

    // Create .git directory
    fs::create_dir_all(&git_dir)?;

    // Create necessary subdirectories
    fs::create_dir_all(git_dir.join("objects"))?;
    fs::create_dir_all(git_dir.join("refs/heads"))?;

    // Create HEAD file
    let mut head_file = fs::File::create(git_dir.join("HEAD"))?;
    writeln!(head_file, "ref: refs/heads/master")?;

    // Create config file (optional)
    let mut config_file = fs::File::create(git_dir.join("config"))?;
    writeln!(config_file, "[core]")?;
    writeln!(config_file, "\trepositoryformatversion = 0")?;
    
    Ok(())
}
