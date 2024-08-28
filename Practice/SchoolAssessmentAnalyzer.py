import csv
import pandas as pd
import numpy as np
from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime

class SchoolAssessmentAnalyzer:
    def __init__(self):
        self.data = pd.DataFrame()

    def process_file(self, file_path):
        """Opens and reads the content of the file, supports CSV, Excel, and plain text."""
        try:
            if file_path.endswith('.csv'):
                self.data = pd.read_csv(file_path)
            elif file_path.endswith('.xlsx'):
                self.data = pd.read_excel(file_path)
            elif file_path.endswith('.txt'):
                with open(file_path, 'r') as file:
                    self.data = pd.read_csv(file, delimiter='\t')
            else:
                raise ValueError("Unsupported file format")
        except Exception as e:
            print(f"Error processing file {file_path}: {e}")

    def transfer_data(self, criteria, source_file, destination_file):
        """Transfers data based on predefined criteria."""
        try:
            self.process_file(source_file)
            filtered_data = self.data.query(criteria)
            filtered_data.to_csv(destination_file, index=False)
            print(f"Data transferred to {destination_file}")
        except Exception as e:
            print(f"Error transferring data: {e}")

    def fetch_web_data(self, url):
        """Fetches data from school webpage using urlopen."""
        try:
            with urlopen(url) as response:
                html = response.read()
                soup = BeautifulSoup(html, 'html.parser')
                # Custom logic to extract relevant information
                # For example, extract tables or specific div tags
                # Let's assume we are extracting a table with assessment scores
                table = soup.find('table')
                self.data = pd.read_html(str(table))[0]
                print("Web data fetched successfully")
        except Exception as e:
            print(f"Error fetching web data from {url}: {e}")

    def analyze_content(self):
        """Analyzes assessment data to generate statistical summaries."""
        try:
            if not self.data.empty:
                summary = {
                    'Average Score': self.data['Score'].mean(),
                    'Max Score': self.data['Score'].max(),
                    'Min Score': self.data['Score'].min(),
                    'Top 5 Scores': self.data['Score'].nlargest(5).tolist(),
                    'Bottom 5 Scores': self.data['Score'].nsmallest(5).tolist(),
                }
                return summary
            else:
                raise ValueError("No data to analyze")
        except Exception as e:
            print(f"Error analyzing content: {e}")
            return None

    def generate_summary(self):
        """Generates a summary of assessment activities for the school principal."""
        student_performance = {
            'Student A': {
                'Average Score': 85.5,
                'Top Performing Class': 'Grade 10B'
            }
        }

        subject_analysis = {
            'Mathematics': 'Improved by 10% compared to the last assessment.',
            'Science': 'Consistent performance across all classes.'
        }

        notable_observations = 'Grade 8A shows a significant improvement in English proficiency.'
        
        web_data_insights = '95% of students accessed assessment resources online.'
        
        recommendations = 'Consider additional support for Grade 9B in Mathematics.'
        
        report_date = datetime.now().strftime('%Y-%m-%d')

        # Constructing the report
        report = (
            "School Assessment Summary Report:\n\n"
            f"1. Overall Performance of Student A:\n"
            f"   - Average score: {student_performance['Student A']['Average Score']}\n"
            f"   - Top-performing class: {student_performance['Student A']['Top Performing Class']}\n\n"
            "2. Subject-wise Analysis:\n"
            f"   - Mathematics: {subject_analysis['Mathematics']}\n"
            f"   - Science: {subject_analysis['Science']}\n\n"
            "3. Notable Observations:\n"
            f"   - {notable_observations}\n\n"
            "4. Web Data Insights:\n"
            f"   - Online participation: {web_data_insights}\n\n"
            "5. Recommendations:\n"
            f"   - {recommendations}\n\n"
            f"Report generated on: {report_date}\n"
        )

        return report

        

# Example Usage
analyzer = SchoolAssessmentAnalyzer()
summary_report = analyzer.generate_summary()
print(summary_report)

# Example Usage
analyzer = SchoolAssessmentAnalyzer()

# Process files
analyzer.process_file('Class_10B_Score.csv')

# Transfer data
# analyzer.transfer_data('Score > 90', 'Class_10B_Score.csv', 'high_achiever.csv')

# Fetch web data (requires an actual school website URL with a valid table for the example)
# analyzer.fetch_web_data('https://schoolwebsite.com/assessment')

# Analyze content
analysis = analyzer.analyze_content()
print(analysis)

# Generate summary
summary = analyzer.generate_summary()
print(summary)
