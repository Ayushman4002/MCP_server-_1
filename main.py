from fastmcp import FastMCP
import random 
import json

#Create the fastMCP server instance
mcp = FastMCP("Simple Calculator Server")

# TOLL: Add two numbers
@mcp.tool
def add(a: int,b: int)->int:
    """Add two numbers together.
        Args.
            a (int): The first number.
            b (int): The second number.
        Returns:
            int: The sum of the two numbers.
        """   
    return a + b

#tool : genertae a random number between two numbers
@mcp.tool
def random_number(min: int, max: int) -> int:
    """Generate a random number between two numbers.
        Args.
            min (int): The minimum number.
            max (int): The maximum number.
        Returns:
            int: A random number between the two numbers.
        """
    return random.randint(min, max)


# Resource: Server information
@mcp.resource("info://server")
def server_info() -> str:
    """"Get information about this server"""
    info = {
        "name" : "Simple Calculator Server",
        "version" : "1.0.0",
        "description" : "A simple calculator server that can add two numbers.",
        "tools" : ["add", "random_number"],
        "authors" : ["Kabir Bahuguna"]
    }
    return json.dumps(info,indent = 2)

# start the server
if __name__ == "__main__":
    mcp.run(transport="http", host="localhost", port=8000)

# to run this you will writ ein you terminal: fastmcp run server.py --transport http --host localhost --port 8000