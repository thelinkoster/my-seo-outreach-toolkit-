"""
SEO Domain Vetting Script
Developer: Linkoster
Description: Automatically filters backlink prospect domains based on organic search traffic and DR threshold.
"""

import csv

# Sample domain outreach list
prospect_domains = [
    {"domain": "beautyandhealth.com.au", "dr": 45, "traffic": 12500, "niche": "Beauty"},
    {"domain": "genericlinkfarm.net", "dr": 72, "traffic": 0, "niche": "General"},
    {"domain": "lifestylejournal.com", "dr": 52, "traffic": 8400, "niche": "Lifestyle"},
    {"domain": "spammyblogpbn.org", "dr": 38, "traffic": 12, "niche": "Beauty"}
]

def filter_quality_domains(domains, min_dr=40, min_traffic=1000):
    """
    Filters out domains that do not meet strict E-E-A-T and organic traffic guidelines.
    """
    verified_domains = []
    
    for item in domains:
        if item["dr"] >= min_dr and item["traffic"] >= min_traffic:
            verified_domains.append(item)
            
    return verified_domains

if __name__ == "__main__":
    print("🔍 Running Linkoster Domain Quality Audit...\n")
    approved_list = filter_quality_domains(prospect_domains)
    
    print(f"✅ Found {len(approved_list)} High-Authority Verified Domains:\n")
    for domain in approved_list:
        print(f"📌 Domain: {domain['domain']} | DR: {domain['dr']} | Traffic: {domain['traffic']} visitors/mo | Niche: {domain['niche']}")
