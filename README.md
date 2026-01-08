# Color Addition Data Generator 🎨

A physics simulation data generator for **additive color mixing tasks**. This generator creates scenarios where two colored balls move toward each other and merge, requiring models to predict and animate the additive color mixture that results from their combination.

---

## 📋 Table of Contents

- [Quick Start](#-quick-start)
- [Project Structure](#-project-structure)
- [Output Format](#-output-format)
- [Configuration & Color Physics](#️-configuration--color-physics)
- [Generated Prompts & Examples](#-generated-prompts--examples)
- [Usage Examples](#-usage-examples)
- [Core Components](#-core-components)
- [Technical Implementation](#-technical-implementation)
- [Troubleshooting](#-troubleshooting)

---

## 🚀 Quick Start

### 1. Clone and Setup Environment

```bash
# Navigate to the generator directory
cd O-16_color_addition_data_generator

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
pip install -e .
```

### 2. Generate Test Data

```bash
# Generate 10 samples (without videos, faster)
python examples/generate.py --num-samples 10 --no-videos

# Generate 100 samples (with videos)
python examples/generate.py --num-samples 100

# Specify output directory and random seed
python examples/generate.py --num-samples 50 --output data/my_output --seed 42
```

### 3. View Generated Results

Generated data will be saved in `data/questions/{domain}_task/` directory, with each task in its own folder.

---

## 📁 Project Structure

```
O-16_color_addition_data_generator/
├── core/                    # 🔧 Framework utilities
│   ├── base_generator.py   # Abstract base class
│   ├── schemas.py          # Pydantic models (TaskPair, etc.)
│   ├── image_utils.py      # Image rendering helpers
│   ├── video_utils.py      # MP4 video generation
│   └── output_writer.py    # Standardized file output
├── src/                     # 🎨 Color mixing implementation
│   ├── generator.py        # Additive color physics & animation
│   ├── prompts.py          # Color mixing prompt templates
│   └── config.py           # Ball properties & mixing parameters
├── examples/
│   └── generate.py         # Generation script
└── data/questions/         # Generated color mixing scenarios
    └── color_addition_task/
        └── color_addition_XXXX/
            ├── first_frame.png     # Two separated colored balls
            ├── final_frame.png     # Single merged ball with mixed color
            ├── prompt.txt          # Task instructions
            └── ground_truth.mp4    # Ball merging animation
```

### File Descriptions

**Core Framework (`core/`)** - Framework utilities:
- `base_generator.py`: Abstract base class and configuration
- `schemas.py`: TaskPair data model (no rubrics)
- `image_utils.py`: PIL image rendering helpers  
- `video_utils.py`: MP4 video generation with OpenCV
- `output_writer.py`: File output in standardized format

**Color Addition Implementation (`src/`)**:
- `config.py`: Ball properties and color mixing parameters
- `generator.py`: Additive RGB physics and animation logic
- `prompts.py`: Color mixing prompt templates

---

## 📦 Output Format

Each color addition task generates:

```
data/questions/color_addition_task/color_addition_XXXX/
├── first_frame.png      # Two colored balls at separate positions
├── final_frame.png      # Single merged ball with additive color
├── prompt.txt           # Color mixing task instructions
└── ground_truth.mp4     # Animation showing balls merging
```

**Example Task Components:**
- **Initial State**: Two colored balls (e.g., red + blue) positioned apart
- **Final State**: Single ball with additive mixed color (e.g., magenta) 
- **Animation**: Smooth ball movement with real-time color mixing in overlapping regions
- **Prompt**: "Two circular balls with different colors... move toward each other... additive color mixture..."

---

## ⚙️ Configuration & Color Physics

### Key Color Mixing Settings (`src/config.py`)

```python
class TaskConfig(GenerationConfig):
    # Task Identity
    domain: str = Field(default="color_addition")
    image_size: tuple[int, int] = Field(default=(512, 512))
    
    # Ball Properties
    ball_radius: int = Field(default=60, description="Radius of the circular balls")
    min_distance: float = Field(default=200, description="Minimum distance between ball centers")
    edge_margin: int = Field(default=80, description="Margin from image edges")
    
    # Video Generation
    generate_videos: bool = Field(default=True, description="Create MP4 animations")
    video_fps: int = Field(default=10, description="Animation frame rate")
```

### Color Physics Implementation

- **Additive RGB Mixing**: R₁+R₂, G₁+G₂, B₁+B₂
- **Normalization**: Proportional scaling when sum exceeds 255
- **Color Range**: 50-255 per channel (avoids too-dark colors)
- **Real-time Mixing**: Pixel-perfect overlap detection during animation

### Advanced Animation Features

**Sophisticated Overlap Handling**:
- **Pixel-perfect detection** using NumPy coordinate grids
- **Three rendering regions**: Ball1-only, Ball2-only, Overlap
- **Real-time color mixing** in overlap areas during animation
- **Preserved original colors** in non-overlapping regions

**Color Mixing Algorithm**:
```python
# Additive mixing with normalization
mixed_r = color1[0] + color2[0]
mixed_g = color1[1] + color2[1] 
mixed_b = color1[2] + color2[2]

# Proportional scaling if any channel > 255
if max(mixed_r, mixed_g, mixed_b) > 255:
    scale = 255.0 / max_value
    # Apply scaling to all channels
```

**Motion Physics**:
- **Linear interpolation** for smooth ball movement
- **Equal speeds** toward calculated midpoint
- **25 transition frames** + hold frames for clear visualization

### Generated Prompts & Examples

**Sample Generated Prompts** (from actual examples):
- *"Two circular balls with different colors are positioned at different locations. Animate the balls moving toward each other at the same speed until they completely merge as one. When the balls overlap, the overlapping region should display the additive color mixture of their original colors."*
- *"Two colored circular balls start at different positions. They move toward each other at equal speeds until they fully overlap and merge into one. The overlapping region during movement and the final merged ball should show the additive color mixture of the two original ball colors."*

**Task Requirements**:
- ✅ Two different colored balls at separate positions
- ✅ Equal movement speeds toward midpoint
- ✅ Additive color mixing in overlap regions
- ✅ Complete merging with final mixed color
- ✅ Smooth animation throughout process

### Example Color Combinations

**Generated Color Mixing Examples:**
- **Red + Pink** → Bright Red/Orange (normalized RGB addition)
- **Blue + Yellow** → Light Yellow/Beige (complementary mixing)
- **Brown + Lavender** → Peachy/Tan (complex RGB combination)

**Color Generation Range:**
- Each RGB channel: 50-255 (avoids too-dark colors)
- Ensures visible, interesting mixing results
- Proper normalization when sum exceeds 255

---

## 💡 Usage Examples

```bash
# Generate 50 color mixing tasks
python examples/generate.py --num-samples 50

# Quick test with 3 samples
python examples/generate.py --num-samples 3 --seed 42

# Fast generation without videos  
python examples/generate.py --num-samples 100 --no-videos

# Custom output directory
python examples/generate.py --num-samples 10 --output data/my_colors

# View all options
python examples/generate.py --help
```

---

## 🧠 Core Components

### TaskPair Schema

The `TaskPair` data structure contains:

- `task_id`: Unique identifier (e.g., `"color_addition_0001"`)
- `domain`: Always `"color_addition"`
- `prompt`: Task instruction text
- `first_image`: Two separate colored balls (PIL Image)
- `final_image`: Single merged ball with mixed color (PIL Image)
- `ground_truth_video`: MP4 animation path (optional)

### Color Physics

**Additive RGB Mixing Formula:**
```python
mixed_color = (
    min(255, color1[0] + color2[0]),  # Red channel
    min(255, color1[1] + color2[1]),  # Green channel  
    min(255, color1[2] + color2[2])   # Blue channel
)

# With proportional normalization if any channel > 255
if max(mixed_color) > 255:
    scale_factor = 255.0 / max(mixed_color)
    mixed_color = tuple(int(c * scale_factor) for c in mixed_color)
```

---

## 🎯 Technical Implementation

### Animation Pipeline

1. **Color Generation**: Two random colors (RGB 50-255 per channel)
2. **Position Calculation**: Valid placements with minimum distance constraint
3. **Motion Physics**: Linear interpolation toward exact midpoint
4. **Overlap Detection**: Pixel-perfect masking using NumPy coordinate grids
5. **Color Mixing**: Real-time additive RGB in overlapping regions
6. **Video Generation**: 25 transition frames + hold frames at 10 FPS

### Pixel-Perfect Overlap Algorithm

```python
# Create coordinate grids for efficient computation
y_coords, x_coords = np.ogrid[:height, :width]

# Distance from each ball center
dist1 = np.sqrt((x_coords - ball1_x)**2 + (y_coords - ball1_y)**2)
dist2 = np.sqrt((x_coords - ball2_x)**2 + (y_coords - ball2_y)**2)

# Define regions
ball1_mask = dist1 <= radius
ball2_mask = dist2 <= radius  
overlap_mask = ball1_mask & ball2_mask
```

---

## ✨ Quality Features

### Visual Excellence

- **High Resolution**: 512x512 images for clear detail
- **Visible Colors**: RGB range 50-255 prevents too-dark balls
- **Smooth Animation**: 25 transition frames with hold periods
- **Clean Rendering**: Black outlines for ball visibility

### Physics Accuracy

- **Correct Additive Mixing**: Proper RGB channel addition
- **Normalization**: Proportional scaling when values exceed 255  
- **Linear Motion**: Equal speeds toward calculated midpoint
- **Collision Detection**: Pixel-perfect overlap boundaries

### Reproducibility

- **Seeded Generation**: `--seed 42` for consistent results
- **Configurable Parameters**: All physics values in `TaskConfig`
- **Consistent Output**: Standardized file naming and structure

---

## 🔧 Troubleshooting

### Import Errors
```bash
# ModuleNotFoundError: No module named 'core'
pip install -e .
```

### Video Generation Issues
```bash
# OpenCV not available
pip install opencv-python==4.10.0.84

# Skip videos for faster generation
python examples/generate.py --num-samples 50 --no-videos
```

### Performance Issues
```bash
# Large datasets - generate in batches
python examples/generate.py --num-samples 100 --no-videos

# Memory issues - reduce image size in src/config.py
image_size: tuple[int, int] = Field(default=(256, 256))
```

### Color Issues
- Colors too dark: Adjust color range in `src/generator.py` (increase min from 50)
- Mixing looks wrong: Check additive formula in `_generate_task_data()`
- Balls too small: Increase `ball_radius` in `src/config.py`

---

## 📝 Quick Start Checklist

Before generating color addition tasks:

- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Package installed (`pip install -e .`)
- [ ] Test generation: `python examples/generate.py --num-samples 3 --seed 42`
- [ ] Verify output contains: `first_frame.png`, `final_frame.png`, `prompt.txt`, `ground_truth.mp4`
- [ ] Check colors look reasonable and balls merge correctly
- [ ] Confirm additive color mixing appears accurate

---

**Output**: Each color addition task includes initial state image, final merged state image, task prompt, and optional MP4 animation demonstrating the complete additive color mixing process. 🎨✨
