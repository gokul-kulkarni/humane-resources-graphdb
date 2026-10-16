import os
from neo4j import GraphDatabase
from dotenv import load_dotenv

load_dotenv()

NEO4J_URI=os.getenv("NEO4J_URI")
NEO4J_USERNAME=os.getenv("NEO4J_USERNAME")
NEO4J_PASSWORD=os.getenv("NEO4J_PASSWORD")
NEO4J_DATABASE=os.getenv("NEO4J_DATABASE")

driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USERNAME, NEO4J_PASSWORD))

driver.verify_connectivity()
print("successfully connected to NEO4J")

query = """
CREATE
(eng: Department {name: "Engineering"}),
(data: Department {name: "Data"}),
(fin: Department {name: "Finance"}),
(ceo: Employee {name: "Sarah", role: "CEO"}),
(ehead: Employee {name: "Alice", role: "Head of Engineering"}),
(dhead: Employee {name: "Bob", role: "Head of Data"}),
(eng1: Employee {name: "Carol", role: "Software Engineer"}),
(data1: Employee {name: "David", role: "Data Scientist"}),
(fin1: Employee {name: "Emma", role: "Finance Analyst"}),
(ehead)-[:REPORTS_TO]->(ceo),
(dhead)-[:REPORTS_TO]->(ceo),
(en1)-[:REPORTS_TO]->(ehead),
(data1)-[:REPORTS_TO]->(dhead),
(fin1)-[:REPORTS_TO]->(ceo),
(ehead)-[:WORKS_IN]->(eng),
(eng1)-[:WORKS_IN]->(eng),
(dhead)-[:WORKS_IN]->(data),
(data1)-[:WORKS_IN]->(data),
(fin1)-[:WORKS_IN]->(fin)
"""

driver.execute_query(query, database=NEO4J_DATABASE)
print("Company Org chart created successfully")

def main() -> None:
    print("Hello from humanresourcegraphdb!")
