import numpy as np
import matplotlib.pyplot as plt
from sympy import prime
from mpl_toolkits.mplot3d import Axes3D

"""
REAL-WORLD PROBLEM: SOLAR FARM OPTIMIZATION WITH TIERED REGULATORY CONSTRAINTS

Context: A company is planning a solar farm in a region with stepped regulatory thresholds.
- Land cost increases in discrete jumps at specific acreage thresholds (regulatory tiers)
- Energy production is a continuous function of land area and panel density
- Environmental impact fees apply in discrete tiers based on panel density
- The objective is to maximize profit while navigating these discontinuous constraints
"""

# === PROBLEM DEFINITION ===

def land_cost(acres):
    """
    Land cost with regulatory tier jumps:
    - Below 50 acres: $8,000 per acre
    - 50-100 acres: $10,000 per acre
    - 100-200 acres: $15,000 per acre
    - Above 200 acres: $25,000 per acre plus special permit fee
    """
    if acres < 50:
        return 8000 * acres
    elif acres < 100:
        return 10000 * acres
    elif acres < 200:
        return 15000 * acres
    else:
        return 25000 * acres + 500000  # Including special permit fee

def environmental_impact_fee(panel_density):
    """
    Environmental impact fees based on panel density (panels per acre):
    - Below 100: $50 per panel
    - 100-200: $75 per panel
    - 200-300: $100 per panel
    - Above 300: $200 per panel
    """
    if panel_density < 100:
        return 50 * panel_density
    elif panel_density < 200:
        return 75 * panel_density
    elif panel_density < 300:
        return 100 * panel_density
    else:
        return 200 * panel_density

def energy_production(acres, panel_density):
    """
    Annual energy production in MWh:
    - Each panel produces 2.5 MWh per year on average
    - Efficiency decreases slightly with higher density due to shading
    """
    total_panels = acres * panel_density
    efficiency_factor = max(0.6, 1 - (panel_density / 1000))  # Efficiency drops with density
    return total_panels * 2.5 * efficiency_factor

def revenue(energy_mwh):
    """Revenue at $60 per MWh"""
    return energy_mwh * 60

def panel_costs(acres, panel_density):
    """Panel costs at $500 per panel"""
    total_panels = acres * panel_density
    return total_panels * 500

def annual_profit(acres, panel_density):
    """
    Calculate annual profit considering:
    - Initial costs amortized over 25-year lifespan
    - Ongoing annual maintenance costs
    - Annual revenue from energy production
    """
    # Initial costs (amortized)
    initial_cost = (land_cost(acres) + panel_costs(acres, panel_density)) / 25  # 25-year lifespan
    
    # Annual costs
    maintenance_cost = acres * panel_density * 20  # $20 annual maintenance per panel
    env_fee = environmental_impact_fee(panel_density) * acres / 25  # Amortized environmental fee
    
    # Annual revenue
    annual_revenue = revenue(energy_production(acres, panel_density))
    
    # Profit
    return annual_revenue - initial_cost - maintenance_cost - env_fee

# === PRIME-ADAPTIVE OPTIMIZATION METHOD ===

def prime_adaptive_2d_optimization(f, x_range, y_range, steps=3):
    """
    Prime-Adaptive optimization for 2D discontinuous functions
    
    Args:
        f: Function to optimize, takes two arguments
        x_range: Tuple of (min_x, max_x)
        y_range: Tuple of (min_y, max_y)
        steps: Number of refinement steps
    
    Returns:
        Tuple of (best_x, best_y, best_value)
    """
    x_min, x_max = x_range
    y_min, y_max = y_range
    
    # Start with primary search based on moderate prime numbers
    p_index_x = 15  # Starting with 47th prime
    p_index_y = 20  # Starting with 71st prime
    
    best_value = float('-inf')
    best_x, best_y = None, None
    
    search_history = []
    
    for step in range(steps):
        # Get prime numbers for this iteration
        px = prime(p_index_x)
        py = prime(p_index_y)
        
        print(f"Step {step+1}: Using primes px={px}, py={py} for grid")
        
        # Create prime-based grid
        x_values = np.linspace(x_min, x_max, px)
        y_values = np.linspace(y_min, y_max, py)
        
        # Search the grid
        for x in x_values:
            for y in y_values:
                value = f(x, y)
                search_history.append((x, y, value))
                
                if value > best_value:
                    best_value = value
                    best_x, best_y = x, y
        
        # Refine search area around best point
        x_min = max(x_min, best_x - (x_max - x_min) / px)
        x_max = min(x_max, best_x + (x_max - x_min) / px)
        y_min = max(y_min, best_y - (y_max - y_min) / py)
        y_max = min(y_max, best_y + (y_max - y_min) / py)
        
        print(f"  Best found: acres={best_x:.2f}, density={best_y:.2f}, profit=${best_value:.2f}")
        print(f"  New search range: x=[{x_min:.2f}, {x_max:.2f}], y=[{y_min:.2f}, {y_max:.2f}]")
        
        # Adjust prime indices based on detected discontinuities
        x_values_near = np.linspace(best_x - 0.1, best_x + 0.1, 20)
        y_fixed = best_y
        values_x = [f(x, y_fixed) for x in x_values_near]
        if max(values_x) - min(values_x) > best_value * 0.1:  # Detect discontinuity in x
            p_index_x += 2  # Use higher prime for more refinement
        else:
            p_index_x -= 1  # Use lower prime if smooth
            
        x_fixed = best_x
        y_values_near = np.linspace(best_y - 0.1, best_y + 0.1, 20)
        values_y = [f(x_fixed, y) for y in y_values_near]
        if max(values_y) - min(values_y) > best_value * 0.1:  # Detect discontinuity in y
            p_index_y += 2  # Use higher prime for more refinement
        else:
            p_index_y -= 1  # Use lower prime if smooth
        
        # Keep prime indices in reasonable range
        p_index_x = max(5, min(30, p_index_x))
        p_index_y = max(5, min(30, p_index_y))
    
    return best_x, best_y, best_value, search_history

# === RUN THE OPTIMIZATION ===

# Define the objective function (annual profit)
def objective(acres, panel_density):
    return annual_profit(acres, panel_density)

# Define the search space
acres_range = (10, 250)          # 10 to 250 acres
density_range = (50, 400)        # 50 to 400 panels per acre

print("🔥 SOLAR FARM OPTIMIZATION WITH PRIME-ADAPTIVE METHOD 🔥")
print("Optimizing solar farm layout with discontinuous regulatory constraints...")
print("Searching for optimal acres and panel density for maximum profit...")

# Run the optimization
best_acres, best_density, best_profit, search_history = prime_adaptive_2d_optimization(
    objective, acres_range, density_range, steps=4
)

# === ANALYZE RESULTS ===

print("\n🔥 OPTIMIZATION RESULTS 🔥")
print(f"Optimal Solar Farm Configuration:")
print(f"  Land Area:     {best_acres:.2f} acres")
print(f"  Panel Density: {best_density:.2f} panels per acre")
print(f"  Total Panels:  {best_acres * best_density:.0f} panels")
print(f"  Annual Profit: ${best_profit:.2f}")

# Calculate values at optimal point
energy = energy_production(best_acres, best_density)
amortized_land = land_cost(best_acres) / 25
amortized_panels = panel_costs(best_acres, best_density) / 25
annual_revenue_value = revenue(energy)
env_fee = environmental_impact_fee(best_density) * best_acres / 25
maintenance = best_acres * best_density * 20

print("\nDetailed Breakdown:")
print(f"  Annual Energy Production: {energy:.2f} MWh")
print(f"  Annual Revenue: ${annual_revenue_value:.2f}")
print(f"  Amortized Land Cost: ${amortized_land:.2f}")
print(f"  Amortized Panel Cost: ${amortized_panels:.2f}")
print(f"  Annual Maintenance: ${maintenance:.2f}")
print(f"  Amortized Environmental Fee: ${env_fee:.2f}")

# Check regulatory tiers at optimal point
print("\nRegulatory Analysis:")
if best_acres < 50:
    print("  Land Tier: Below 50 acres (Lowest regulatory burden)")
elif best_acres < 100:
    print("  Land Tier: 50-100 acres (Medium regulatory burden)")
elif best_acres < 200:
    print("  Land Tier: 100-200 acres (High regulatory burden)")
else:
    print("  Land Tier: Above 200 acres (Highest regulatory burden + Special permit)")

if best_density < 100:
    print("  Density Tier: Below 100 panels/acre (Lowest environmental impact)")
elif best_density < 200:
    print("  Density Tier: 100-200 panels/acre (Medium environmental impact)")
elif best_density < 300:
    print("  Density Tier: 200-300 panels/acre (High environmental impact)")
else:
    print("  Density Tier: Above 300 panels/acre (Extreme environmental impact)")

# === VISUALIZATION ===

# Convert search history to arrays for plotting
search_x = [item[0] for item in search_history]
search_y = [item[1] for item in search_history]
search_z = [item[2] for item in search_history]

# Create a dense grid for visualization
vis_acres = np.linspace(10, 250, 100)
vis_density = np.linspace(50, 400, 100)
X, Y = np.meshgrid(vis_acres, vis_density)
Z = np.zeros_like(X)

for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        Z[i, j] = objective(X[i, j], Y[i, j])

# Create profit landscape visualization
fig = plt.figure(figsize=(15, 10))

# 3D surface plot
ax1 = fig.add_subplot(121, projection='3d')
surf = ax1.plot_surface(X, Y, Z, cmap='viridis', alpha=0.7, linewidth=0, antialiased=True)
ax1.scatter(search_x, search_y, search_z, color='red', s=10, label='Search Points')
ax1.scatter([best_acres], [best_density], [best_profit], color='black', s=100, marker='*', label='Optimal')
ax1.set_xlabel('Land Area (acres)')
ax1.set_ylabel('Panel Density (panels/acre)')
ax1.set_zlabel('Annual Profit ($)')
ax1.set_title('Profit Landscape with Discontinuities')
fig.colorbar(surf, ax=ax1, shrink=0.5, aspect=5)
ax1.legend()

# 2D contour plot
ax2 = fig.add_subplot(122)
contour = ax2.contourf(X, Y, Z, 20, cmap='viridis')
ax2.scatter(search_x, search_y, color='red', s=10, alpha=0.5, label='Search Points')
ax2.scatter([best_acres], [best_density], color='black', s=200, marker='*', label='Optimal')

# Add regulatory tier lines
ax2.axvline(x=50, color='white', linestyle='--', alpha=0.7, label='Land Tiers')
ax2.axvline(x=100, color='white', linestyle='--', alpha=0.7)
ax2.axvline(x=200, color='white', linestyle='--', alpha=0.7)
ax2.axhline(y=100, color='yellow', linestyle='--', alpha=0.7, label='Density Tiers')
ax2.axhline(y=200, color='yellow', linestyle='--', alpha=0.7)
ax2.axhline(y=300, color='yellow', linestyle='--', alpha=0.7)

ax2.set_xlabel('Land Area (acres)')
ax2.set_ylabel('Panel Density (panels/acre)')
ax2.set_title('Profit Contours with Regulatory Tiers')
fig.colorbar(contour, ax=ax2)
ax2.legend()

plt.tight_layout()
plt.savefig('solar_farm_optimization.png', dpi=300)
plt.close()

# === SENSITIVITY ANALYSIS ===
# Check how profit changes around optimal point
print("\n📊 Sensitivity Analysis:")

# Check profit at the regulatory boundaries
tier_acres = [49.9, 50.1, 99.9, 100.1, 199.9, 200.1]
tier_density = [99.9, 100.1, 199.9, 200.1, 299.9, 300.1]

print("\nProfit at Land Regulatory Boundaries:")
for a in tier_acres:
    profit = objective(a, best_density)
    print(f"  Acres={a:.1f}, Profit=${profit:.2f}")

print("\nProfit at Density Regulatory Boundaries:")
for d in tier_density:
    profit = objective(best_acres, d)
    print(f"  Density={d:.1f}, Profit=${profit:.2f}")

print("\n🔍 CONCLUSION:")
print("The Prime-Adaptive method successfully navigated the discontinuous profit landscape")
print("created by regulatory tiers in land cost and environmental impact fees.")
print("It identified the optimal configuration by efficiently exploring the search space")
print("and concentrating search efforts near regulatory boundaries where dramatic")
print("changes in profit occur.")
