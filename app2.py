import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit.components.v1 as components
import base64

# Load your dataset (assuming it's already prepared)
# Replace 'rfm.csv' with the actual path to your dataset
data = pd.read_csv('./rmfclv.csv')

data['CLV'] = (data['Frequency'] * data['Monetary']) - data['Recency']

# Function to display visualizations based on selected KPI
def display_visualization(kpi,container):
    with container:
        if kpi == "CLV":
            components.html(
        f'<iframe title="CLV" width="600" height="373.5" src="https://app.powerbi.com/view?r=eyJrIjoiNTQ4YzdiYzktMWZjNC00ZDdkLWJjYWItZGMwZTUyZjlkYzMxIiwidCI6IjExMTNiZTM0LWFlZDEtNGQwMC1hYjRiLWNkZDAyNTEwYmU5MSIsImMiOjN9" frameborder="0" allowFullScreen="true"></iframe>',
        height=600
    )

        elif kpi == "CAC":
            components.html(
        f'<iframe title="Hackathon" width="600" height="373.5" src="https://app.powerbi.com/view?r=eyJrIjoiMzIzOTQ1NzEtMDEwNi00ZmY1LTljNDQtMGIwMGQzYmY0OWM0IiwidCI6IjExMTNiZTM0LWFlZDEtNGQwMC1hYjRiLWNkZDAyNTEwYmU5MSIsImMiOjN9" frameborder="0" allowFullScreen="true"></iframe>',
        height=600
    )

            
        elif kpi == "Gross Sales":
            components.html(
        f'<iframe title="hackathon(gross sales)" width="600" height="373.5" src="https://app.powerbi.com/view?r=eyJrIjoiY2Y3YjYxOGItZjBiMC00NWVlLWE4MWUtOGFhM2VlNWQ2NmZjIiwidCI6IjExMTNiZTM0LWFlZDEtNGQwMC1hYjRiLWNkZDAyNTEwYmU5MSIsImMiOjN9" frameborder="0" allowFullScreen="true"></iframe>',
        height=600
    )

        elif kpi == "Burn Rate":
              components.html(
        f'<iframe title="Final Hackathon" width="600" height="373.5" src="https://app.powerbi.com/view?r=eyJrIjoiNmU0OTBiYmItYmQ2MS00MzA2LTkwODYtYTBjNTVkNWQ1M2FlIiwidCI6IjExMTNiZTM0LWFlZDEtNGQwMC1hYjRiLWNkZDAyNTEwYmU5MSIsImMiOjN9" frameborder="0" allowFullScreen="true"></iframe>',
        height=600
    )


def generate_nlp_recommendations(kpi, container):
    with container:

        if kpi == "CAC":
            df = pd.read_csv('./cacData.csv')
            df["Revenue"] = df["New_Customers"] * df["ARPU_value"]

            # Define thresholds for actionable insights
            
            roi_threshold = 0.05, 
            cac_threshold = 100,  
            high_spend_threshold = df['Marketing_Spend'].mean()  
            

            # Initialize actionable insights
            insights = []

            # Actionable Insight 1: High ROI campaigns
            high_roi = df[df['ROI_value'] > roi_threshold]
            insights.append(f"{len(high_roi)} campaigns have an ROI above {roi_threshold}. Scale these campaigns to maximize revenue.")

            # Actionable Insight 2: Low ROI campaigns
            low_roi = df[df['ROI_value'] < roi_threshold]
            insights.append(f"{len(low_roi)} campaigns have an ROI below {roi_threshold}. Focus on optimizing these campaigns for better returns.Keep track of all kinds of data. Having a good understanding of how your audience is behaving and interacting with your content is one of the most valuable things you can do for your marketing campaigns.")

            # Actionable Insight 3: High CAC campaigns
            high_cac = df[df['CAC'] > cac_threshold]
            insights.append(f"{len(high_cac)} campaigns have a CAC above ${cac_threshold}. Focus on improving customer targeting and reducing acquisition costs which can be achieved by dividing your audience into smaller groups with similar characteristics to deliver personalized campaigns that resonate better.")

            # Actionable Insight 4: Underutilized High ROI campaigns
            underutilized_high_roi = df[(df['ROI_value'] > roi_threshold) & (df['Marketing_Spend'] < high_spend_threshold / 2)]
            insights.append(f"{len(underutilized_high_roi)} campaigns have high ROI but low spend. Consider increasing investment in these campaigns as they can perform better with better reach.")

            # Actionable Insight 5: High Spend campaigns
            high_spend = df[df['Marketing_Spend'] > high_spend_threshold]
            insights.append(f"{len(high_spend)} campaigns have marketing spend above the average (${high_spend_threshold:.2f}). Ensure these campaigns justify their investment.")

            # Actionable Insight 6: Focus on High ARPU channels
            high_arpu_channels = df.groupby('Marketing_Channel')['ARPU_value'].mean().idxmax()
            insights.append(f"The highest ARPU is in the {high_arpu_channels} channel. Focus more resources on this channel to maximize returns.")

            # Actionable Insight 7: Low-converting campaigns
            low_converting = df[df['New_Customers'] < df['New_Customers'].mean()]
            insights.append(f"{len(low_converting)} campaigns have below-average customer acquisition. Improve ad targeting and conversion strategies.")

            # Actionable Insight 8: Retarget Existing Customers
            insights.append("Use retargeting campaigns to upsell or cross-sell to existing customers. Focus on high ARPU customers for better ROI.")

            # Actionable Insight 9: Reallocate budget from inefficient campaigns
            inefficient_campaigns = df[(df['ROI_value'] < roi_threshold) & (df['Marketing_Spend'] > high_spend_threshold)]
            insights.append(f"{len(inefficient_campaigns)} campaigns have high spend but low ROI. Reallocate budgets to more efficient campaigns.")

            # Actionable Insight 10: Predict future campaign success
            insights.append("Use historical ROI and CAC metrics to predict future campaign success and prioritize investments in high-performing strategies.")

            # Print actionable insights
            st.write(f"Actionable Insights for {kpi}:")
            for insight in insights:
                st.write(f"- {insight}")
    
        elif kpi == "CLV":
            # Load your dataset
            df = pd.read_csv('newData.csv')

            # Define thresholds and average metrics
            thresholds = {
                "Recency": 30,  # Days since the last purchase; lower is better
                "Frequency": 50,  # Minimum frequency of purchases
                "Monetary": 75000,  # Minimum acceptable monetary value
                "CLV": 5000000,  # High-value customers based on CLV
            }

            # Compute average metrics for the dataset
            avg_monetary = df["Monetary"].mean()
            avg_frequency = df["Frequency"].mean()

            # Initialize insights list
            insights = []

            # Generate insights
            # Insight 1: Inactive customers who haven't purchased recently
            inactive_customers = df[df["Recency"] > thresholds["Recency"]]
            if not inactive_customers.empty:
                insights.append(f"{len(inactive_customers)} customers have not purchased in over {thresholds['Recency']} days. "
                                f"Run email or ad campaigns to re-engage them.")

            # Insight 2: High-value customers based on CLV
            high_value_customers = df[df["CLV"] > thresholds["CLV"]]
            if not high_value_customers.empty:
                insights.append(f"{len(high_value_customers)} high-value customers with CLV above ${thresholds['CLV']:.2f}. "
                                f"Focus on loyalty programs and personalized offers for them.")

            # Insight 3: Frequent purchasers with low monetary value
            low_monetary_high_frequency = df[(df["Monetary"] < avg_monetary) & (df["Frequency"] > avg_frequency)]
            if not low_monetary_high_frequency.empty:
                insights.append(f"{len(low_monetary_high_frequency)} customers purchase frequently but spend below average. "
                                f"Promote bundle offers or upselling strategies to increase their spend.")

            # Insight 4: High spenders who purchase infrequently
            high_monetary_low_frequency = df[(df["Monetary"] > avg_monetary) & (df["Frequency"] < avg_frequency)]
            if not high_monetary_low_frequency.empty:
                insights.append(f"{len(high_monetary_low_frequency)} customers spend above average but purchase infrequently. "
                                f"Encourage repeat purchases through subscription services or reminders.")

            # Insight 5: Recently acquired high-value customers
            recent_high_value_customers = df[(df["Recency"] <= thresholds["Recency"]) & (df["CLV"] > thresholds["CLV"])]
            if not recent_high_value_customers.empty:
                insights.append(f"{len(recent_high_value_customers)} newly acquired customers with CLV above ${thresholds['CLV']:.2f}. "
                                f"Engage them with welcome offers and exceptional service.")

            # Insight 6: Customers with low frequency and monetary value
            low_value_customers = df[(df["Frequency"] < avg_frequency) & (df["Monetary"] < avg_monetary)]
            if not low_value_customers.empty:
                insights.append(f"{len(low_value_customers)} customers have low frequency and spend. "
                                f"Focus marketing efforts on converting them into repeat customers.")

            # Insight 7: Top-performing customers with high CLV and frequency
            top_customers = df[(df["CLV"] > thresholds["CLV"]) & (df["Frequency"] > thresholds["Frequency"])]
            if not top_customers.empty:
                insights.append(f"{len(top_customers)} top-performing customers with high CLV and purchase frequency. "
                                f"Strengthen these relationships to maintain loyalty.")

            # Insight 8: High-engagement customers with potential for higher spend
            high_engagement_potential = df[(df["Frequency"] > avg_frequency) & (df["Monetary"] < thresholds["Monetary"])]
            if not high_engagement_potential.empty:
                insights.append(f"{len(high_engagement_potential)} customers engage frequently but spend below $75,000. "
                                f"Introduce premium products or exclusive deals.")

            # Insight 9: Customers at risk of churn
            churn_risk_customers = df[(df["Recency"] > thresholds["Recency"]) & (df["Frequency"] < avg_frequency)]
            if not churn_risk_customers.empty:
                insights.append(f"{len(churn_risk_customers)} customers show signs of churning based on recency and frequency. "
                                f"Send win-back campaigns or special offers to retain them.")

            # Insight 10: Customers with high CLV but low recent engagement
            high_value_low_engagement = df[(df["CLV"] > thresholds["CLV"]) & (df["Recency"] > thresholds["Recency"])]
            if not high_value_low_engagement.empty:
                insights.append(f"{len(high_value_low_engagement)} high-value customers have low recent engagement. "
                                f"Re-engage with exclusive offers or personal outreach.")

            st.write(f"Actionable Insights for {kpi}:")
            for insight in insights:
                st.write(f"- {insight}")
        
        elif kpi == "Gross Sales":
            sales_df = pd.read_csv('grossSales.csv')
            # Key Metrics
            metrics = {
                "Total Gross Sales": sales_df['GROSS AMT'].sum(),
                "Average Gross Sales per Customer": sales_df.groupby('CUSTOMER')['GROSS AMT'].sum().mean(),
                "Top Performing Styles by Sales": sales_df.groupby('Style')['GROSS AMT'].sum().sort_values(ascending=False).head(3).to_dict(),
                "Most Common Sizes": sales_df['Size'].value_counts().head(3).to_dict(),
                "Top Customers by Gross Sales": sales_df.groupby('CUSTOMER')['GROSS AMT'].sum().sort_values(ascending=False).head(3).to_dict(),
            }

            # Generate Actionable Insights
            insights = []

            # 1. Promote top-selling styles
            top_styles = metrics["Top Performing Styles by Sales"]
            insights.append(f"Promote the top-selling styles: {', '.join(top_styles.keys())}, as they account for the highest gross sales.")

            # 2. Ensure inventory for popular sizes
            common_sizes = metrics["Most Common Sizes"]
            insights.append(f"Ensure sufficient inventory for popular sizes: {', '.join(common_sizes.keys())}, to meet customer demand.")

            # 3. Focus on high-value customers
            top_customers = metrics["Top Customers by Gross Sales"]
            insights.append(f"Engage high-value customers like {', '.join(top_customers.keys())} with loyalty programs or exclusive offers.")

            # 4. Review underperforming styles
            underperforming_styles = sales_df.groupby('Style')['GROSS AMT'].sum().sort_values(ascending=True).head(3).to_dict()
            insights.append(f"Review and optimize sales strategies for underperforming styles: {', '.join(underperforming_styles.keys())}.")

            # 5. Introduce volume discounts
            avg_rate = sales_df['RATE'].mean()
            insights.append(f"Introduce volume discounts for products with an average rate of ${avg_rate:.2f} to encourage bulk purchases.")


            # 7. Cross-sell and upsell opportunities
            insights.append("Encourage existing customers to purchase complementary products through bundling and personalized recommendations.")

            # 8. Seasonal promotions
            insights.append("Run time-limited promotions during peak shopping seasons to maximize gross sales and customer engagement.")

            # 9. Invest in digital marketing
            insights.append("Increase investment in digital ads for top-selling styles and sizes. Focus campaigns on high-value customers.")

            # 10. Reduce inventory for low-demand items
            low_demand_items = sales_df.groupby('Style')['PCS'].sum().sort_values(ascending=True).head(3).to_dict()
            insights.append(f"Reduce stock for low-demand items like {', '.join(low_demand_items.keys())} to minimize waste and reduce costs.")

            insights.append("Focus on Cross-Selling and Upselling High-Demand Styles and Complementary Products.Analyze your top-performing styles, for e.g., SET268, J0277, and identify complementary products frequently purchased together. Create bundled offers that incentivize customers to purchase additional items. For example: Pair high-demand styles with lower-performing complementary items at a discount and use targeted recommendations on your e-commerce platform")

            st.write(f"Actionable Insights for {kpi}:")
            for insight in insights:
                st.write(f"- {insight}")
        
        elif kpi == "Burn Rate":
            file_path = "./burnRate.csv"  # Replace with the actual file path
            burn_rate_df = pd.read_csv(file_path)
            # Generate actionable insights for burn rate analysis
            insights = []
            # Insight 1: Calculate months until cash runs out
            burn_rate_df['Months_to_Cash_Runout'] = burn_rate_df['Cash_Reserves'] / burn_rate_df['Net_Burn_Rate']
            low_cash_runout = burn_rate_df[burn_rate_df['Months_to_Cash_Runout'] < 6]
            insights.append(f"{len(low_cash_runout)} companies have less than 6 months of cash runway. Focus on securing funding or reducing costs.")

            # Insight 2: High burn rate companies
            high_burn_rate_threshold = burn_rate_df['Net_Burn_Rate'].mean() + burn_rate_df['Net_Burn_Rate'].std()
            high_burn_rate_companies = burn_rate_df[burn_rate_df['Net_Burn_Rate'] > high_burn_rate_threshold]
            insights.append(f"{len(high_burn_rate_companies)} companies have a high burn rate. Focus on optimizing operational expenses.")

            # Insight 3: High salaries contributing to burn rate
            high_salary_companies = burn_rate_df[burn_rate_df['Salaries'] > burn_rate_df['Salaries'].mean()]
            insights.append(f"{len(high_salary_companies)} companies have above-average salaries contributing significantly to their burn rate. Consider evaluating staffing levels.")

            # Insight 4: High R&D spending
            high_rd_companies = burn_rate_df[burn_rate_df['R&D'] > burn_rate_df['R&D'].mean()]
            insights.append(f"{len(high_rd_companies)} companies have above-average R&D spending. Ensure alignment of R&D expenses with long-term business goals.")

            # Insight 5: High other costs
            high_other_costs = burn_rate_df[burn_rate_df['Other_Costs'] > burn_rate_df['Other_Costs'].mean()]
            insights.append(f"{len(high_other_costs)} companies have above-average other costs. Review these discretionary expenses for potential savings.")

            # Insight 6: Monitor validation costs
            if 'Validation' in burn_rate_df.columns:
                high_validation_costs = burn_rate_df[burn_rate_df['Validation'] > burn_rate_df['Validation'].mean()]
                insights.append(f"{len(high_validation_costs)} companies are incurring significant validation costs. Prioritize low-cost alternatives for validation.")

            # Insight 7: Optimize cash reserves
            low_cash_reserves = burn_rate_df[burn_rate_df['Cash_Reserves'] < burn_rate_df['Cash_Reserves'].mean()]
            insights.append(f"{len(low_cash_reserves)} companies have below-average cash reserves. Focus on increasing runway through fundraising or revenue generation.")

            # Insight 8: Improve cost efficiency for high-burn companies
            high_burn_low_efficiency = burn_rate_df[(burn_rate_df['Net_Burn_Rate'] > burn_rate_df['Net_Burn_Rate'].mean()) & (burn_rate_df['Salaries'] + burn_rate_df['R&D'] + burn_rate_df['Other_Costs'] > burn_rate_df['Net_Burn_Rate'])]
            insights.append(f"{len(high_burn_low_efficiency)} companies have operational inefficiencies contributing to high burn rates. Reevaluate cost structures.")

            # Insight 9: Diversify funding sources
            diversify_funding_needed = burn_rate_df[burn_rate_df['Months_to_Cash_Runout'] < 9]
            insights.append(f"{len(diversify_funding_needed)} companies should explore diversified funding sources like venture debt or grants.")

            # Insight 10: Plan for long-term runway
            burn_rate_df['Adjusted_Cash_Runout'] = burn_rate_df['Cash_Reserves'] / (burn_rate_df['Net_Burn_Rate'] + burn_rate_df[['Salaries', 'R&D', 'Other_Costs']].sum(axis=1))
            short_runway_companies = burn_rate_df[burn_rate_df['Adjusted_Cash_Runout'] < 12]
            insights.append(f"{len(short_runway_companies)} companies have less than 12 months of runway even after cost adjustments. Focus on long-term financial planning.")

            # Print insights
            st.write(f"Actionable Insights for {kpi}:")
            for insight in insights:
                st.write(f"- {insight}")

            


if "view" not in st.session_state:
    st.session_state.view = "Default"  # Default view

# Sidebar for KPI selection
st.sidebar.title("Select a KPI")
selected_kpi = st.sidebar.selectbox(
    "Choose a KPI:",
    ["CAC", "Gross Sales", "Burn Rate", "CLV"]
)

if st.sidebar.button("Show Visualization"):
    st.session_state.view = "Visualization"
if st.sidebar.button("Generate Recommendations"):
    st.session_state.view = "Recommendations"

# Create a container for the output
output_container = st.container()

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    return f"data:image/jpg;base64,{encoded_string}"

# Render content based on the selected view
if st.session_state.view == "Visualization":
    display_visualization(selected_kpi, output_container)
elif st.session_state.view == "Recommendations":
    generate_nlp_recommendations(selected_kpi, output_container)
else:
    # Default background and message
    with output_container:
        bg_image = add_bg_from_local('biztech.jpg')
        st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{bg_image}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
        )
        st.markdown(
        """
        <div style="text-align: center; color: white; padding: 50px; background-color: rgba(0,0,0,0.5);">
            <h1>Welcome to the KPI Dashboard</h1>
            <p>Select a KPI and choose a view to get started!</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
        
    


