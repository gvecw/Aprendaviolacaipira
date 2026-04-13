import os
import re
import urllib.request
from urllib.parse import urljoin, urlparse

# URL to trace
base_url = "https://sertanejoraizoficial.vercel.app/"

def download_file(url, local_path):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            content = response.read()
        dirname = os.path.dirname(local_path)
        if dirname:
            os.makedirs(dirname, exist_ok=True)
        with open(local_path, 'wb') as f:
            f.write(content)
        print(f"Downloaded {url} to {local_path}")
        return content
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        return None

def main():
    print("Fetching main page...")
    html_content = download_file(base_url, "index.html")
    if not html_content:
        return
    
    html_text = html_content.decode('utf-8')
    
    # regex to find links to css, js, images in src or href
    pattern = re.compile(r'(src|href)="([^"]+)"')
    
    new_html_text = html_text
    
    matches = pattern.findall(html_text)
    print(f"Found {len(matches)} links to process.")
    for attr, link in matches:
        if link.startswith('http') and not link.startswith(base_url):
            continue # Skip external links that aren't on the same domain
            
        if link.startswith('data:') or link.startswith('#'):
            continue
            
        full_url = urljoin(base_url, link)
        parsed_url = urlparse(full_url)
        
        # Only download if it's on the same domain or a known CDN if necessary
        # Actually, let's download everything we can that is an asset
        if not full_url.endswith(('.html', '/')) or 'fonts' in full_url:
            local_name = parsed_url.path.lstrip('/')
            if not local_name:
                continue
            
            # Simple sanitization
            local_name = urllib.parse.unquote(local_name)
            if '?' in local_name:
                local_name = local_name.split('?')[0]
                
            if download_file(full_url, local_name):
                # Replace the link in the HTML
                # Very simple replace, might be brittle but often works if paths match exactly
                new_html_text = new_html_text.replace(link, local_name)

    with open("index.html", 'w', encoding='utf-8') as f:
        f.write(new_html_text)
    print("Done rewriting index.html")

if __name__ == "__main__":
    main()
