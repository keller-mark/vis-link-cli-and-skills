# vis-link-cli-and-skills

Background: MCP, which is only designed for machines to use, is being replaced by simple CLIs + Skills, which both humans and agents can easily use.

Idea: Create a proof of concept of:
- Frontend web page that renders a visualization. Should be minimal, ideally just an HTML file. Upon loading the page, it connects to the backend websocket server to "request" a SESSION_ID
  - For now, using Vega-Lite
- Backend server: the bridge between the frontend and the CLI. Should be as minimal as possible.
  - Use web sockets
  - Use python
- CLI tool for manipulating the visualization, with the following commands
  - `vislink connect SESSION_ID # Connect to a particular session`
  - `vislink get-spec # Get the current visualization specification`
  - `vislink set-spec # Set the current visualization specification`
  - More fine-grained getters and setters for changing marks/channels/etc. within the spec
 - Agent Skills directory of markdown files, one per CLI command, with concise name and description in frontmatter.

  Tech stack: Use the following technologies:
  - Plain HTML file with modern ESM JavaScript code for frontend
  - Python and Starlette framework for backend
    - Add a route to serve the frontend HTML via a Jinja2 template
  - Python and argparse for CLI
  - UV for python environment
  
