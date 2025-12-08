from dotenv import load_dotenv
from prompts import SESSION_INSTRUCTION, AGENT_INSTRUCTION
from livekit import agents
from livekit.agents import  AgentSession, Agent, RoomInputOptions
from livekit.plugins import (
    google,
    noise_cancellation,
)

from mcp_client import MCPServerSse
from mcp_client.agent_tools import MCPToolsIntegration
import os
# from tools import open_url
from livekit.plugins import tavus


load_dotenv()

class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(instructions=AGENT_INSTRUCTION
                         )


async def my_agent(ctx: agents.JobContext):
    session = AgentSession(
        llm=google.realtime.RealtimeModel(
            model="gemini-2.0-flash-live-001",
            voice="Aoede",
            api_key=os.getenv("GOOGLE_API_KEY"),
        ),
    )

    mcp_server = MCPServerSse(
        params={"url": os.environ.get("N8N_MCP_SERVER_URL")},
        cache_tools_list=True,
        name="SSE MCP Server"
    )

    agent = await MCPToolsIntegration.create_agent_with_tools(
    agent_class=Assistant,
    mcp_servers=[mcp_server]
    )

    avatar = tavus.AvatarSession(
        persona_id=os.environ.get("PERSONA_ID"),
        replica_id=os.environ.get("REPLICA_ID"),
        api_key=os.environ.get("TAVUS_API_KEY"),
    )



    await avatar.start(session, room=ctx.room)

    await session.start(
        room=ctx.room,
        agent=agent,
        room_input_options=RoomInputOptions(
            # LiveKit Cloud enhanced noise cancellation
            # - If self-hosting, omit this parameter
            # - For telephony applications, use `BVCTelephony` for best results
            noise_cancellation=noise_cancellation.BVC(),
        ),
    )


    await ctx.connect()

    await session.generate_reply(
        instructions=SESSION_INSTRUCTION,
    )


if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=my_agent))