# Northwestern Formula Racing Organization

## Data Acquisition Interface Team

### Background
Every year, Northwestern University has a Formula Organization that makes an actual **Formula One** car from scratch and races the car at an annual collegiate race.

I aggregated data coming from the **80** sensors on the car and visualized it for the engineering teams and later on for final competitions.

This repository contains:
- The frontend UI layer of our visualization tool. Since the frontend is required to do a lot of calculations and graphing of data, I preferred Python over JavaScript for this project.

### Technical Skills
- Python
- Streamlit
- Seaborn
- Scikit-learn
- Numpy
- Matplotlib
- Pandas
- Cycler 
- Tkinter GUI

### Technical Stack & Libraries

- Interactive widgets – Selectboxes, file uploaders, buttons, session state management.

### Key Features & Technical Highlights
#### File Ingestion & Data Binding

- Implements client-side reactive data handling, dynamically binding uploaded data to UI components.
- Data is parsed using **Pandas**, leveraging DataFrame operations for dynamic column detection, type inference, and timestamp normalization.
- Enables on-the-fly schema mapping from raw telemetry columns to structured visualization axes.

### Interactive Data Visualization

- Dynamic selection of plot type (Line, Scatter) via st.sidebar.selectbox.
- Real-time two-way binding between user-selected X/Y axes and plotting logic.
- Matplotlib integration with advanced features:
  - cycler for custom color palettes and theme consistency.
  - Dynamic legend, axis labeling, and plot title generation.
- High-performance rendering for large datasets ~1 million rows.
- Optional logarithmic and linear scaling, adjustable markers, and grid control (extensible for engineering-grade visualization needs).

### Geospatial Data Mapping

- Embedded interactive map, plotting telemetry reference points.
- Uses geospatial DataFrames and lat/lon transformations for dynamic marker rendering.
- Can be extended for real-time positional telemetry visualization.

### Frontend Architecture & Reactive UI

- Built with **Streamlit**, a **Python** reactive UI framework supporting:
- Stateful interactivity without page reloads.
- Sidebar-driven component orchestration for user actions.
- Integration of widgets (file uploader, dropdowns, buttons) with Python callbacks.
- Implements frontend state management via session state to persist user interactions across callbacks.

### Integration with Backend Pipelines

- Connects with ourterminal-driven backend to preprocess the binary data from the car (repo linked here:).

### Advanced UI/UX Practices
- Responsive layout (st.set_page_config(layout="wide")) optimized for engineering dashboards.
- Sidebar-driven component hierarchy for structured navigation.
- Immediate feedback loops (success messages, dataframe previews) to enhance usability for data engineers and telemetry analysts.
- Map visualization provides contextual spatial awareness, important in automotive telemetry analysis.

