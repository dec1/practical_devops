# 

## Double Dash (`--`) in commands 

The double dash (`--`) is a special command line argument that serves as a _delimiter_ between **options** and **positional arguments**. It's a convention followed by POSIX-compliant command line tools and many other utilities.

> **Important Note**: In command-line terminology, there are two main types of arguments:
> - **Options** (also called "flags" or "switches"): Arguments that start with hyphens (`-` or `--`) and modify the behavior of the command (e.g., `-v`, `--verbose`)
> - **Positional arguments**: Arguments that don't start with hyphens and are interpreted based on their position in the command (e.g., filenames, paths)
>
> The double dash forces all subsequent arguments to be treated as positional arguments, even if they start with hyphens. This distinction is crucial for understanding when and why to use the double dash.

## Purpose

When a command encounters `--`, it stops interpreting subsequent arguments as options (flags that start with a dash `-`), and instead treats them as positional arguments, even if they begin with a dash.

## Key Use Cases

### 1. Working with files or arguments that begin with a dash

```
# Search for the literal string "-v" in a file
grep -- -v filename.txt

# Remove a file that starts with a dash
rm -- -myfile.txt
```

### 2. Nested commands (command wrappers)

```
# Pass SSH options through a wrapper command
podman machine ssh -- -L 2375:localhost:2375 "command"

# Pass arguments to a command run in a container
docker run alpine -- echo -n "Hello"

# Run a command with sudo, passing options to the command
sudo -- command -xyz
```

### 3. Marking the end of options

```
# Use cp with options, then specify source and destination
cp -r -v -- /source /destination

# List all files, including those starting with dash
ls -la -- *
```

## How It Works

The double dash operates in two main contexts:

### For Simple Commands

When a standard command-line tool parses its arguments:

1. It processes options from left to right (e.g., `-a`, `-b`, `--option`)
2. When it encounters `--`, it stops option processing
3. Everything after `--` is treated as a positional argument

For example, in `grep -- -v filename.txt`:
- Without `--`, grep would interpret `-v` as the "invert match" option
- With `--`, grep treats `-v` as the pattern to search for

### For Command Wrappers

When a command wrapper (that calls another program) processes arguments:

1. The wrapper parses its own arguments until `--`
2. Everything after `--` is collected and passed to the underlying command
3. This creates a clean separation between options for different programs

## Implementation Details

Command wrappers (like `podman machine ssh`) typically:

1. Parse their own arguments up to `--`
2. Take everything after `--` and pass it to the underlying command
3. This creates a clean separation between options for the wrapper and options for the wrapped command

Without this mechanism, it would be difficult or impossible to pass options that might be interpreted by both the wrapper and the wrapped command.

## Common Applications

- Git: `git checkout -- filename` (treat as a file, not a branch)
- SSH: `ssh -- hostname command -options` (pass options to remote command)
- Docker/Podman: `docker exec -- container command -flags`
- Package managers: `npm install -- --save-dev` (pass flags to scripts)
- Command wrappers: `sudo -- command -xyz`

## Best Practices

- Use `--` whenever you need to work with arguments that start with a dash
- Always use `--` when using command wrappers and you need to pass options to the wrapped command
- Consider using `--` with commands like `rm` for safety, especially in scripts