# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a web automation testing project focused on testing a real estate website (visionteamrealestate.com). The project uses Selenium WebDriver to automate browser interactions, specifically testing phone button click functionality and chat system interactions.

## Architecture

### Core Components

- **Python Selenium Scripts**: Main automation logic using Chrome WebDriver
- **Database Administration**: Scripts to manage test database state between runs
- **IP Verification System**: Validates test execution by checking public IP registration in MySQL database
- **JavaScript Browser Library**: Node.js headless browser utilities

### Key Files

- `open_fcw_page.py`: Original automation script that tests phone button clicking
- `vision_team_page_open.py`: Enhanced version with chat system testing and manual intervention capabilities
- `database_admin/database_admin.py`: Database cleanup utilities that execute shell scripts
- `ip_check.py`: IP-based test verification using MySQL queries
- `lib/headless_browser.js`: Node.js module for headless Chrome operations

## Dependencies and Setup

The project uses:
- Python 3.10+ with Selenium WebDriver
- Chrome browser and ChromeDriver
- MySQL database access for verification
- Node.js for JavaScript components

Dependencies are managed via `pyproject.toml`:
```toml
dependencies = [
    "selenium>=4.32.0",
]
```

## Common Commands

### Running Tests
```bash
# Run the enhanced test with chat functionality
python vision_team_page_open.py

# Run IP verification independently
python ip_check.py
```

### Database Management
The DatabaseAdmin class executes external shell scripts located at:
- `/home/adamsl/selenium-headless/mcba_tests/menu_shell_scripts/`

These scripts handle:
- Monitor deletion
- User cleanup (keeping only admin)
- Message deletion
- Conversation cleanup

### Python Package Management
```bash
# Install dependencies
uv sync

# The project uses uv for Python package management
```

## Test Flow Architecture

1. **Database Preparation**: Clear existing test data using DatabaseAdmin
2. **Browser Launch**: Initialize Chrome WebDriver (configurable headless mode)
3. **Page Navigation**: Load target website and capture page source
4. **Element Interaction**: Wait for and click specific UI elements
5. **Verification**: Check database state and IP registration
6. **Cleanup**: Optionally close browser and validate results

## Testing Strategy

The project implements two testing approaches:
- **Automated Testing** (`open_fcw_page.py`): Fully automated with screenshots
- **Interactive Testing** (`vision_team_page_open.py`): Includes manual intervention points with browser alerts

Both scripts share common patterns:
- Implicit and explicit waits for element availability
- JavaScript-based element interactions
- Screenshot capture for debugging
- Database state verification

## External Dependencies

- Shell scripts for database management (external to this repository)
- MySQL database with `wp_mcba_users` table
- Chrome browser installation
- Network access to visionteamrealestate.com and ipify.org