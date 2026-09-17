

# Loads JSON and one other format (XML or YAML — your choice)
# Auto-detect format from file extension
# Raise your ConfigFileNotFoundError when file is missing
# Raise your ConfigParseError for corrupted or invalid files

# Supports value access

# Simple keys: get('robot_id')
# Nested keys with dot notation: get('sensors.ir_count')
# Default values: get('unknown_key', default=0)

# Validates configuration

# Required fields check
# Type validation
# Range validation (e.g., sensor count > 0)
# Raises your ConfigValidationError listing all failures

# Saves configuration

# Write back to file in detected format
# Pretty-printed for readability