from pydantic import BaseModel

# Schemas for Workout table endpoints
# -------------------------------------------------------------------------------------------------------
# [BASE]


# Information to get sent via QR code to the mirror for creating a workout
# and uploading workout information
class MirrorBase(BaseModel):
    username: str
    workoutID: int
    video_path: str
    keypoints_path: str
    analytics_path: str
