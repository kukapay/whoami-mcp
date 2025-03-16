from mcp.server.fastmcp import FastMCP
import getpass

# Initialize the MCP server
mcp = FastMCP("WhoAmI")

# Define a tool to fetch the current system username
@mcp.tool()
def whoami() -> str:
    """Returns the username of the current system user as my identity."""
    try:
        # Get the current system username using getpass.getuser()
        username = getpass.getuser()
        # Return a simple dictionary with the username
        return username
    except Exception as e:
        # Handle any unexpected errors (e.g., environment issues)
        return {"error": f"Failed to fetch username: {str(e)}"}

# Start the server
if __name__ == "__main__":
    mcp.run()