"""
Eris Phone - AI Technical Support Agent
Main application entry point
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Create FastAPI app
app = FastAPI(
    title="Eris Phone API",
    description="AI-powered technical support system",
    version="0.1.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("CORS_ORIGINS", "http://localhost:3000").split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check endpoint
@app.get("/health")
async def health_check():
    """API health check"""
    return {
        "status": "healthy",
        "service": "eris_phone",
        "version": "0.1.0"
    }

# Support API endpoints
@app.get("/api/v1/categories")
async def get_support_categories():
    """Get available support categories"""
    return {
        "categories": [
            {"id": 1, "name": "Refrigerators", "icon": "❄️"},
            {"id": 2, "name": "Washing Machines", "icon": "🧺"},
            {"id": 3, "name": "Ovens", "icon": "🔥"},
            {"id": 4, "name": "Dishwashers", "icon": "🍽️"},
            {"id": 5, "name": "Televisions", "icon": "📺"},
            {"id": 6, "name": "Microwaves", "icon": "📶"},
            {"id": 7, "name": "General Appliances", "icon": "⚡"},
        ]
    }

@app.post("/api/v1/support/ticket")
async def create_support_ticket(issue: dict):
    """Create new support ticket and process with AI"""
    return {
        "ticket_id": "TKT-001",
        "status": "processing",
        "message": "Processing your issue..."
    }

@app.get("/api/v1/solutions/{category_id}")
async def get_solutions(category_id: int):
    """Get self-help solutions for category"""
    solutions = {
        1: [  # Refrigerators
            {
                "id": 1,
                "title": "Defrost Refrigerator",
                "description": "Ice buildup in freezer",
                "steps": [
                    "Unplug refrigerator",
                    "Remove frozen items",
                    "Place towels on floor",
                    "Wait 4-8 hours for ice to melt",
                    "Plug back in"
                ],
                "difficulty": "easy",
                "time_minutes": 480
            },
            {
                "id": 2,
                "title": "Improve Energy Efficiency",
                "description": "Refrigerator using too much electricity",
                "steps": [
                    "Clean condenser coils at back",
                    "Check door seals for damage",
                    "Set temperature to 37-38°F",
                    "Don't overfill the fridge",
                    "Allow hot food to cool first"
                ],
                "difficulty": "easy",
                "time_minutes": 30
            }
        ],
        2: [  # Washing Machines
            {
                "id": 3,
                "title": "Clean Washing Machine Drain",
                "description": "Water not draining properly",
                "steps": [
                    "Stop the wash cycle",
                    "Locate drain hose",
                    "Remove hose carefully",
                    "Use plunger or snake to clear blockage",
                    "Reconnect hose",
                    "Run test cycle"
                ],
                "difficulty": "medium",
                "time_minutes": 45
            },
            {
                "id": 4,
                "title": "Remove Bad Odors",
                "description": "Washing machine smells bad",
                "steps": [
                    "Run empty hot water cycle",
                    "Add 2 cups white vinegar",
                    "Run another empty cycle",
                    "Wipe rubber seal with vinegar",
                    "Leave door open to dry"
                ],
                "difficulty": "easy",
                "time_minutes": 60
            }
        ],
        3: [  # Ovens
            {
                "id": 5,
                "title": "Oven Not Heating",
                "description": "Oven is not reaching desired temperature",
                "steps": [
                    "Check heating element for visible damage",
                    "Turn off power at breaker",
                    "Wait 5 minutes",
                    "Turn power back on",
                    "Test oven temperature with thermometer",
                    "If still not working, call technician"
                ],
                "difficulty": "medium",
                "time_minutes": 30
            },
            {
                "id": 6,
                "title": "Oven Glass Door Repair",
                "description": "Glass door is cracked or won't stay up",
                "steps": [
                    "Turn off power to oven",
                    "Open door fully",
                    "Locate support hinges",
                    "Check if hinges need tightening",
                    "Use wrench to tighten bolts",
                    "Test door movement"
                ],
                "difficulty": "hard",
                "time_minutes": 45
            }
        ],
        4: [  # Dishwashers
            {
                "id": 7,
                "title": "Clean Dishwasher Spray Arms",
                "description": "Dishes not getting cleaned properly",
                "steps": [
                    "Remove bottom rack",
                    "Locate spray arms",
                    "Use toothpick to clean small holes",
                    "Rinse under running water",
                    "Reinstall spray arms",
                    "Run test cycle"
                ],
                "difficulty": "easy",
                "time_minutes": 20
            },
            {
                "id": 8,
                "title": "Fix Drainage Issues",
                "description": "Water pooling at bottom of dishwasher",
                "steps": [
                    "Check drain hose for kinks",
                    "Remove drain hose",
                    "Flush with hot water",
                    "Check sink drain for blockage",
                    "Reconnect hose",
                    "Run test cycle"
                ],
                "difficulty": "medium",
                "time_minutes": 40
            }
        ],
        5: [  # Televisions
            {
                "id": 9,
                "title": "Television Won't Turn On",
                "description": "TV not responding to remote or power button",
                "steps": [
                    "Check power cable is firmly connected",
                    "Replace remote batteries",
                    "Try pressing power button directly on TV",
                    "Wait 60 seconds and try again",
                    "Check if power outlet works (plug in lamp)",
                    "Try different power outlet",
                    "If still not working, contact support"
                ],
                "difficulty": "easy",
                "time_minutes": 15
            },
            {
                "id": 10,
                "title": "No Sound from TV",
                "description": "TV has picture but no audio",
                "steps": [
                    "Check volume is not muted (look for mute icon)",
                    "Increase volume using remote",
                    "Check if audio output is set to TV speakers",
                    "Verify HDMI cable connection",
                    "Try different input source",
                    "Restart TV (power off 30 seconds, power on)",
                    "Check TV sound settings in menu"
                ],
                "difficulty": "easy",
                "time_minutes": 20
            },
            {
                "id": 11,
                "title": "Dead Pixels or Dark Spots",
                "description": "Black dots or dead pixels on screen",
                "steps": [
                    "Check HDMI cable connections",
                    "Try different HDMI input",
                    "Clean screen with soft cloth",
                    "Check if spots appear on all inputs",
                    "Restart TV completely",
                    "If persists, may be hardware issue requiring service"
                ],
                "difficulty": "medium",
                "time_minutes": 25
            }
        ],
        6: [  # Microwaves
            {
                "id": 12,
                "title": "Microwave Not Heating",
                "description": "Food not getting hot in microwave",
                "steps": [
                    "Check power cord is connected",
                    "Verify outlet works",
                    "Let microwave cool for 20 minutes",
                    "Restart microwave",
                    "Test with water in microwave-safe container",
                    "If still not working, contact technician"
                ],
                "difficulty": "easy",
                "time_minutes": 30
            }
        ]
    }
    return {"solutions": solutions.get(category_id, [])}

@app.get("/api/v1/tickets/{ticket_id}")
async def get_ticket_status(ticket_id: str):
    """Get ticket status and history"""
    return {
        "ticket_id": ticket_id,
        "status": "in_progress",
        "category": "Washing Machines",
        "created_at": "2026-05-16T10:00:00Z",
        "last_update": "2026-05-16T14:30:00Z"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
