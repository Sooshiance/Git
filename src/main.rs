mod initialization;

use std::env;
use std::process;

fn main() {
    let args: Vec<String> = env::args().collect();

    if args.len() < 2 {
        eprintln!("Usage: {} <command> [options] [path]", args[0]);
        process::exit(1);
    }

    match args[1].as_str() {
        "init" => {
            let path = if args.len() > 2 { &args[2] } else { "." };
            if let Err(e) = initialization::init_repo(path) {
                eprintln!("Error initializing repository: {}", e);
                process::exit(1);
            }
            println!("Initialized empty Git repository in {}", path);
        }
        _ => {
            eprintln!("Unknown command");
            process::exit(1);
        }
    }
}
