

# 🛠️ multi_nmap_scanner

This is a simple script I made for **Bug Bounty** recon — when you’ve got hundreds of domains and just wanna **quickly scan all of them with Nmap** without doing it one by one.

---

## 💡 What It Does

- Reads a list of domains or IPs from a file  
- Runs Nmap with `-sC -sV` on each target  
- Saves each result to a separate output file (`<target>_output.txt`)  
- Does it all **multi-threaded** for speed

---

## 🔧 Requirements

- Python 3+
- Nmap installed and available in your terminal

Install (if you're starting fresh):

```bash
pip install -r requirements.txt
```

But tbh, the script uses only standard libraries, so nothing extra needed.

---

## 🚀 Usage

```bash
python multi_nmap_scanner.py domains.txt
```

- `domains.txt`: One domain or IP per line

---

## 📁 Example

**domains.txt**
```
example.com
scanme.nmap.org
1.1.1.1
```

**Output:**
```
[+] Scanning example.com...
[✓] Scan of example.com completed. Results saved to example.com_output.txt
...
```

You'll get output files like:
- `example.com_output.txt`
- `scanme.nmap.org_output.txt`
- `1.1.1.1_output.txt`

---

## 🧠 Why I Made This

Bug bounty grind.  
Got hundreds of subdomains?  
Don’t wanna open a new terminal tab for each one?  
Boom — one script, one run, multi-threaded, done.

---

## ⚙️ Default Nmap Flags

- `-sC`: Default scripts
- `-sV`: Service/version detection

You can edit the script to add more flags like `-A`, `-Pn`, etc. if you want.

---

## ⚠️ Notes

- Max threads = 10 (you can tweak it)
- Doesn’t do live host checking — assumes targets are up
- Good idea to throttle if you're scanning production stuff

---

## 🧑‍💻 License

No license, no warranty, use at your own risk.  
If you break something, that’s on you 😅

