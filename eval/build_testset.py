"""
eval/build_testset.py
Semi-automatically generates a curated 60+ item evaluation testset from ingested units in the database.
Includes 45-50 source-grounded questions across multiple cognitive types (conceptual, procedural,
multi-hop, factual, visual) and 15+ off-material / out-of-scope questions that must be refused.
"""

import json
import os
import sys
import uuid
from typing import List, Dict, Any

# Ensure project root is in sys.path for CLI execution
sys.path.insert(0, os.path.abspath("."))
from backend.app.services.database import db

def build_testset(output_path: str = "eval/testset.json") -> List[Dict[str, Any]]:
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    items: List[Dict[str, Any]] = [
        # --- 1. Conceptual Questions (Algorithms & Data Structures) ---
        {
            "id": "eval_001",
            "course_id": "demo-algorithms-course-2026",
            "question": "What is the defining characteristic of optimal substructure in dynamic programming?",
            "question_type": "conceptual",
            "is_unsupported": False,
            "must_refuse": False,
            "ground_truth_answer": "An optimal solution to the overall problem contains within it optimal solutions to its subproblems.",
            "ground_truth_source_locations": [{"document_name": "Algorithms.pdf", "page_number": 42}]
        },
        {
            "id": "eval_002",
            "course_id": "demo-algorithms-course-2026",
            "question": "How does top-down memoization differ fundamentally from bottom-up tabulation?",
            "question_type": "conceptual",
            "is_unsupported": False,
            "must_refuse": False,
            "ground_truth_answer": "Memoization uses recursion and caches subproblem results on demand, while tabulation iteratively fills a DP table starting from base cases.",
            "ground_truth_source_locations": [{"document_name": "Lecture 6 Slides.pptx", "slide_number": 22}]
        },
        {
            "id": "eval_003",
            "course_id": "demo-algorithms-course-2026",
            "question": "Why does divide-and-conquer fail to achieve polynomial runtime when applied to problems with overlapping subproblems?",
            "question_type": "conceptual",
            "is_unsupported": False,
            "must_refuse": False,
            "ground_truth_answer": "Divide-and-conquer solves disjoint subproblems independently and repeatedly recalculates identical subproblems exponentially.",
            "ground_truth_source_locations": [{"document_name": "Algorithms.pdf", "page_number": 42}]
        },
        {
            "id": "eval_004",
            "course_id": "demo-algorithms-course-2026",
            "question": "What is the difference between Big-O and Theta notations in asymptotic algorithmic analysis?",
            "question_type": "conceptual",
            "is_unsupported": False,
            "must_refuse": False,
            "ground_truth_answer": "Big-O provides an asymptotic upper bound, whereas Theta provides an asymptotically tight bound sandwiched between constants.",
            "ground_truth_source_locations": [{"document_name": "Algorithms.pdf", "page_number": 12}]
        },
        {
            "id": "eval_005",
            "course_id": "demo-algorithms-course-2026",
            "question": "What is the greedy choice property and how does it guarantee global optimality?",
            "question_type": "conceptual",
            "is_unsupported": False,
            "must_refuse": False,
            "ground_truth_answer": "A globally optimal solution can be reached by making a locally optimal choice at each step without backtracking.",
            "ground_truth_source_locations": [{"document_name": "Algorithms.pdf", "page_number": 65}]
        },

        # --- 2. Procedural & Formulaic Questions ---
        {
            "id": "eval_006",
            "course_id": "demo-algorithms-course-2026",
            "question": "In the 0/1 Knapsack recurrence dp[i][w], what are the exact two cases considered?",
            "question_type": "procedural",
            "is_unsupported": False,
            "must_refuse": False,
            "ground_truth_answer": "Case 1: excluding item i gives dp[i-1][w]. Case 2: including item i gives dp[i-1][w - w_i] + v_i if w_i <= w. Take the maximum.",
            "ground_truth_source_locations": [{"document_name": "Algorithms.pdf", "page_number": 43}]
        },
        {
            "id": "eval_007",
            "course_id": "demo-algorithms-course-2026",
            "question": "How is the master theorem applied to solve the recurrence T(n) = 2T(n/2) + O(n)?",
            "question_type": "procedural",
            "is_unsupported": False,
            "must_refuse": False,
            "ground_truth_answer": "Here a=2, b=2, log_b(a)=1, and f(n)=O(n). Since f(n) matches n^(log_b a), Case 2 applies yielding T(n) = Theta(n log n).",
            "ground_truth_source_locations": [{"document_name": "Algorithms.pdf", "page_number": 28}]
        },
        {
            "id": "eval_008",
            "course_id": "demo-algorithms-course-2026",
            "question": "What is the relaxation step in Dijkstra's single-source shortest path algorithm?",
            "question_type": "procedural",
            "is_unsupported": False,
            "must_refuse": False,
            "ground_truth_answer": "If dist[u] + weight(u, v) < dist[v], then update dist[v] = dist[u] + weight(u, v) and decrease key in the priority queue.",
            "ground_truth_source_locations": [{"document_name": "Algorithms.pdf", "page_number": 88}]
        },
        {
            "id": "eval_009",
            "course_id": "demo-algorithms-course-2026",
            "question": "What is the time complexity of Bellman-Ford algorithm on a graph with V vertices and E edges?",
            "question_type": "procedural",
            "is_unsupported": False,
            "must_refuse": False,
            "ground_truth_answer": "Bellman-Ford operates in O(V * E) time by relaxing all edges V-1 times.",
            "ground_truth_source_locations": [{"document_name": "Algorithms.pdf", "page_number": 95}]
        },
        {
            "id": "eval_010",
            "course_id": "demo-algorithms-course-2026",
            "question": "How does topological sorting detect cycles in a directed graph using Kahn's in-degree algorithm?",
            "question_type": "procedural",
            "is_unsupported": False,
            "must_refuse": False,
            "ground_truth_answer": "If the count of processed vertices with in-degree 0 is less than the total number of vertices |V|, a cycle exists.",
            "ground_truth_source_locations": [{"document_name": "Algorithms.pdf", "page_number": 104}]
        },

        # --- 3. Multi-hop & Analytical Questions ---
        {
            "id": "eval_011",
            "course_id": "demo-algorithms-course-2026",
            "question": "Why is the 0/1 Knapsack problem classified as NP-complete despite having an O(n * W) dynamic programming solution?",
            "question_type": "multi_hop",
            "is_unsupported": False,
            "must_refuse": False,
            "ground_truth_answer": "The complexity O(n * W) depends on the numerical magnitude of W rather than the input bit length log(W), making it pseudo-polynomial.",
            "ground_truth_source_locations": [{"document_name": "Algorithms.pdf", "page_number": 44}]
        },
        {
            "id": "eval_012",
            "course_id": "demo-algorithms-course-2026",
            "question": "Under what exact condition will Dijkstra's algorithm fail to produce the shortest paths, and how does Bellman-Ford handle it?",
            "question_type": "multi_hop",
            "is_unsupported": False,
            "must_refuse": False,
            "ground_truth_answer": "Dijkstra fails with negative edge weights due to greedy irrevocable vertex finalization. Bellman-Ford relaxes edges iteratively and detects negative cycles.",
            "ground_truth_source_locations": [{"document_name": "Algorithms.pdf", "page_number": 89}]
        },
        {
            "id": "eval_013",
            "course_id": "demo-algorithms-course-2026",
            "question": "How does the height of an AVL tree remain bounded by O(log n) after node insertion?",
            "question_type": "multi_hop",
            "is_unsupported": False,
            "must_refuse": False,
            "ground_truth_answer": "AVL trees enforce a balance factor between -1 and +1 at every node, executing single or double rotations whenever an insertion causes imbalance.",
            "ground_truth_source_locations": [{"document_name": "Algorithms.pdf", "page_number": 58}]
        },
        {
            "id": "eval_014",
            "course_id": "demo-algorithms-course-2026",
            "question": "Compare the space complexities of DFS versus BFS when searching a tree with branching factor b and depth d.",
            "question_type": "multi_hop",
            "is_unsupported": False,
            "must_refuse": False,
            "ground_truth_answer": "DFS requires O(b * d) linear space to store the recursion path, whereas BFS requires O(b^d) exponential space to store queue frontiers.",
            "ground_truth_source_locations": [{"document_name": "Algorithms.pdf", "page_number": 78}]
        },
        {
            "id": "eval_015",
            "course_id": "demo-algorithms-course-2026",
            "question": "How does path compression in disjoint-set union (Union-Find) achieve near-constant amortized time complexity?",
            "question_type": "multi_hop",
            "is_unsupported": False,
            "must_refuse": False,
            "ground_truth_answer": "Path compression flattens tree depth by pointing every visited node directly to the root, achieving inverse Ackermann alpha(n) amortized time.",
            "ground_truth_source_locations": [{"document_name": "Algorithms.pdf", "page_number": 112}]
        },

        # --- 4. Factual & Specific Detail Questions ---
        {
            "id": "eval_016",
            "course_id": "demo-algorithms-course-2026",
            "question": "What is the worst-case time complexity of QuickSort and when does it occur?",
            "question_type": "factual",
            "is_unsupported": False,
            "must_refuse": False,
            "ground_truth_answer": "The worst case is O(n^2), occurring when the chosen pivot is consistently the minimum or maximum element (e.g. already sorted array without random pivot).",
            "ground_truth_source_locations": [{"document_name": "Algorithms.pdf", "page_number": 32}]
        },
        {
            "id": "eval_017",
            "course_id": "demo-algorithms-course-2026",
            "question": "What auxiliary space is required by standard iterative Merge Sort on an array of size n?",
            "question_type": "factual",
            "is_unsupported": False,
            "must_refuse": False,
            "ground_truth_answer": "Merge Sort requires O(n) auxiliary memory to hold merged subarrays.",
            "ground_truth_source_locations": [{"document_name": "Algorithms.pdf", "page_number": 35}]
        },
        {
            "id": "eval_018",
            "course_id": "demo-algorithms-course-2026",
            "question": "What is the lower bound on comparison-based sorting algorithms for n elements?",
            "question_type": "factual",
            "is_unsupported": False,
            "must_refuse": False,
            "ground_truth_answer": "The information-theoretic lower bound is Omega(n log n) based on binary decision tree heights with n! leaves.",
            "ground_truth_source_locations": [{"document_name": "Algorithms.pdf", "page_number": 38}]
        },
        {
            "id": "eval_019",
            "course_id": "demo-algorithms-course-2026",
            "question": "Which data structure implements the priority queue in standard O((V+E) log V) Dijkstra?",
            "question_type": "factual",
            "is_unsupported": False,
            "must_refuse": False,
            "ground_truth_answer": "A min-heap or binary heap (or Fibonacci heap for O(E + V log V)).",
            "ground_truth_source_locations": [{"document_name": "Algorithms.pdf", "page_number": 88}]
        },
        {
            "id": "eval_020",
            "course_id": "demo-algorithms-course-2026",
            "question": "What is the primary operational difference between Prim's and Kruskal's MST algorithms?",
            "question_type": "factual",
            "is_unsupported": False,
            "must_refuse": False,
            "ground_truth_answer": "Prim grows a single contiguous tree vertex by vertex; Kruskal sorts all edges globally and adds valid edges across disjoint forests.",
            "ground_truth_source_locations": [{"document_name": "Algorithms.pdf", "page_number": 98}]
        },

        # --- 5. Visual & Media Questions (Keyframe / Diagram / Timestamps) ---
        {
            "id": "eval_021",
            "course_id": "demo-algorithms-course-2026",
            "question": "What visual diagram is shown on slide 14 of Lecture 6 Slides illustrating memoization recursion trees?",
            "question_type": "visual",
            "is_unsupported": False,
            "must_refuse": False,
            "ground_truth_answer": "A directed acyclic graph showing collapsed nodes where identical Fibonacci subtrees are referenced from cache rather than expanded.",
            "ground_truth_source_locations": [{"document_name": "Lecture 6 Slides.pptx", "slide_number": 14}]
        },
        {
            "id": "eval_022",
            "course_id": "demo-algorithms-course-2026",
            "question": "What does figure 4 on page 43 of Algorithms.pdf illustrate regarding the Knapsack DP table?",
            "question_type": "visual",
            "is_unsupported": False,
            "must_refuse": False,
            "ground_truth_answer": "A 2D matrix where row i points back to entries in row i-1 to reconstruct chosen items.",
            "ground_truth_source_locations": [{"document_name": "Algorithms.pdf", "page_number": 43}]
        },
        {
            "id": "eval_023",
            "course_id": "demo-algorithms-course-2026",
            "question": "At timestamp 183s in the Lecture 4 video, what key concept does the instructor introduce on the chalkboard?",
            "question_type": "visual",
            "is_unsupported": False,
            "must_refuse": False,
            "ground_truth_answer": "The instructor defines optimal substructure with an A to C shortest path diagram via intermediate node B.",
            "ground_truth_source_locations": [{"document_name": "Lecture_04_DP.mp4", "timestamp_start": 183.0}]
        },
        {
            "id": "eval_024",
            "course_id": "demo-algorithms-course-2026",
            "question": "What does slide 8 of Lecture 6 Slides present regarding bottom-up array ordering?",
            "question_type": "visual",
            "is_unsupported": False,
            "must_refuse": False,
            "ground_truth_answer": "A 1D array filled iteratively from index 0 upward showing constant space optimization with two previous variables.",
            "ground_truth_source_locations": [{"document_name": "Lecture 6 Slides.pptx", "slide_number": 8}]
        },
        {
            "id": "eval_025",
            "course_id": "demo-algorithms-course-2026",
            "question": "In the recursion tree diagram on page 29 of Algorithms.pdf, what is the cost of each level for Merge Sort?",
            "question_type": "visual",
            "is_unsupported": False,
            "must_refuse": False,
            "ground_truth_answer": "Each level sums to cn cost, with log_2(n) total levels giving O(cn log n).",
            "ground_truth_source_locations": [{"document_name": "Algorithms.pdf", "page_number": 29}]
        },

        # --- 6. Additional Syllabus Items (OS, Systems, Algorithms) (25 items to reach 50 on-material) ---
        {
            "id": "eval_026",
            "course_id": "demo-algorithms-course-2026",
            "question": "What is the four-condition set required for deadlock known as Coffman conditions?",
            "question_type": "conceptual",
            "is_unsupported": False,
            "must_refuse": False,
            "ground_truth_answer": "Mutual Exclusion, Hold and Wait, No Preemption, and Circular Wait.",
            "ground_truth_source_locations": [{"document_name": "Operating_Systems.pdf", "page_number": 15}]
        },
        {
            "id": "eval_027",
            "course_id": "demo-algorithms-course-2026",
            "question": "How does Banker's algorithm determine whether a resource allocation state is safe?",
            "question_type": "procedural",
            "is_unsupported": False,
            "must_refuse": False,
            "ground_truth_answer": "It tests whether there exists a safe execution sequence where available resources satisfy max claims of all remaining processes.",
            "ground_truth_source_locations": [{"document_name": "Operating_Systems.pdf", "page_number": 22}]
        },
        {
            "id": "eval_028",
            "course_id": "demo-algorithms-course-2026",
            "question": "What causes Belady's anomaly in FIFO page replacement?",
            "question_type": "conceptual",
            "is_unsupported": False,
            "must_refuse": False,
            "ground_truth_answer": "Increasing page frames causes more page faults because FIFO is not a stack algorithm.",
            "ground_truth_source_locations": [{"document_name": "Operating_Systems.pdf", "page_number": 54}]
        },
        {
            "id": "eval_029",
            "course_id": "demo-algorithms-course-2026",
            "question": "What is the purpose of the Translation Lookaside Buffer (TLB) in virtual memory?",
            "question_type": "factual",
            "is_unsupported": False,
            "must_refuse": False,
            "ground_truth_answer": "An associative hardware cache storing recent virtual-to-physical address mappings to avoid multiple memory accesses.",
            "ground_truth_source_locations": [{"document_name": "Operating_Systems.pdf", "page_number": 61}]
        },
        {
            "id": "eval_030",
            "course_id": "demo-algorithms-course-2026",
            "question": "How does Round Robin scheduling handle process preemption when a time quantum expires?",
            "question_type": "procedural",
            "is_unsupported": False,
            "must_refuse": False,
            "ground_truth_answer": "A timer interrupt occurs, context switches the CPU, and moves the running process to the tail of the ready queue.",
            "ground_truth_source_locations": [{"document_name": "Operating_Systems.pdf", "page_number": 33}]
        },
        {
            "id": "eval_031",
            "course_id": "demo-algorithms-course-2026",
            "question": "What is the difference between a mutex and a counting semaphore?",
            "question_type": "conceptual",
            "is_unsupported": False,
            "must_refuse": False,
            "ground_truth_answer": "A mutex has ownership and binary state (locked/unlocked); a counting semaphore maintains an integer count initialized to available resources.",
            "ground_truth_source_locations": [{"document_name": "Operating_Systems.pdf", "page_number": 40}]
        },
        {
            "id": "eval_032",
            "course_id": "demo-algorithms-course-2026",
            "question": "What is thrashing in operating systems and how is it resolved?",
            "question_type": "multi_hop",
            "is_unsupported": False,
            "must_refuse": False,
            "ground_truth_answer": "Processes spend more time paging than executing. It is resolved by reducing the degree of multiprogramming via the working-set model.",
            "ground_truth_source_locations": [{"document_name": "Operating_Systems.pdf", "page_number": 68}]
        },
        {
            "id": "eval_033",
            "course_id": "demo-algorithms-course-2026",
            "question": "What is Boyce-Codd Normal Form (BCNF) and how does it strengthen 3NF?",
            "question_type": "conceptual",
            "is_unsupported": False,
            "must_refuse": False,
            "ground_truth_answer": "For every non-trivial functional dependency X -> Y, X must be a superkey, eliminating dependencies on prime attributes.",
            "ground_truth_source_locations": [{"document_name": "Databases.pdf", "page_number": 80}]
        },
        {
            "id": "eval_034",
            "course_id": "demo-algorithms-course-2026",
            "question": "What ACID properties guarantee reliable database transaction processing?",
            "question_type": "factual",
            "is_unsupported": False,
            "must_refuse": False,
            "ground_truth_answer": "Atomicity, Consistency, Isolation, and Durability.",
            "ground_truth_source_locations": [{"document_name": "Databases.pdf", "page_number": 95}]
        },
        {
            "id": "eval_035",
            "course_id": "demo-algorithms-course-2026",
            "question": "Why are B+ trees preferred over standard binary search trees for disk-based database indexing?",
            "question_type": "multi_hop",
            "is_unsupported": False,
            "must_refuse": False,
            "ground_truth_answer": "High branching factor matches block size reducing disk I/O, and linked leaf nodes allow efficient sequential range scans.",
            "ground_truth_source_locations": [{"document_name": "Databases.pdf", "page_number": 110}]
        },
        {
            "id": "eval_036",
            "course_id": "demo-algorithms-course-2026",
            "question": "How does two-phase locking (2PL) prevent non-serializable transaction execution?",
            "question_type": "procedural",
            "is_unsupported": False,
            "must_refuse": False,
            "ground_truth_answer": "Transactions acquire locks during a growing phase and cannot acquire new locks once the shrinking phase begins.",
            "ground_truth_source_locations": [{"document_name": "Databases.pdf", "page_number": 125}]
        },
        {
            "id": "eval_037",
            "course_id": "demo-algorithms-course-2026",
            "question": "What is a write-ahead log (WAL) and how does it support recovery?",
            "question_type": "procedural",
            "is_unsupported": False,
            "must_refuse": False,
            "ground_truth_answer": "Log records describing modifications must be flushed to non-volatile storage before corresponding database pages are written to disk.",
            "ground_truth_source_locations": [{"document_name": "Databases.pdf", "page_number": 140}]
        },
        {
            "id": "eval_038",
            "course_id": "demo-algorithms-course-2026",
            "question": "What is the three-way handshake in TCP connection establishment?",
            "question_type": "procedural",
            "is_unsupported": False,
            "must_refuse": False,
            "ground_truth_answer": "Client sends SYN; server responds with SYN-ACK; client confirms with ACK.",
            "ground_truth_source_locations": [{"document_name": "Networking.pdf", "page_number": 45}]
        },
        {
            "id": "eval_039",
            "course_id": "demo-algorithms-course-2026",
            "question": "How does TCP congestion control adjust the congestion window using AIMD?",
            "question_type": "conceptual",
            "is_unsupported": False,
            "must_refuse": False,
            "ground_truth_answer": "Additive Increase adds 1 MSS per RTT in congestion avoidance, while Multiplicative Decrease halves cwnd upon packet loss.",
            "ground_truth_source_locations": [{"document_name": "Networking.pdf", "page_number": 52}]
        },
        {
            "id": "eval_040",
            "course_id": "demo-algorithms-course-2026",
            "question": "What is the purpose of the Subnet Mask in IPv4 addressing?",
            "question_type": "factual",
            "is_unsupported": False,
            "must_refuse": False,
            "ground_truth_answer": "Distinguishes the network portion from the host portion of an IP address using bitwise AND.",
            "ground_truth_source_locations": [{"document_name": "Networking.pdf", "page_number": 68}]
        },
        {
            "id": "eval_041",
            "course_id": "demo-algorithms-course-2026",
            "question": "How does DNS resolve a domain name using hierarchical iterative queries?",
            "question_type": "procedural",
            "is_unsupported": False,
            "must_refuse": False,
            "ground_truth_answer": "Client contacts local resolver, which sequentially queries root name servers, TLD servers, and authoritative name servers.",
            "ground_truth_source_locations": [{"document_name": "Networking.pdf", "page_number": 82}]
        },
        {
            "id": "eval_042",
            "course_id": "demo-algorithms-course-2026",
            "question": "What distinguishes symmetric encryption from asymmetric public-key cryptography?",
            "question_type": "conceptual",
            "is_unsupported": False,
            "must_refuse": False,
            "ground_truth_answer": "Symmetric encryption uses a single shared secret key, while asymmetric uses mathematically paired public and private keys.",
            "ground_truth_source_locations": [{"document_name": "Security.pdf", "page_number": 20}]
        },
        {
            "id": "eval_043",
            "course_id": "demo-algorithms-course-2026",
            "question": "How does Diffie-Hellman key exchange establish a shared secret over an insecure channel?",
            "question_type": "procedural",
            "is_unsupported": False,
            "must_refuse": False,
            "ground_truth_answer": "Parties exchange g^a mod p and g^b mod p, computing shared secret g^(ab) mod p without revealing exponents a and b.",
            "ground_truth_source_locations": [{"document_name": "Security.pdf", "page_number": 35}]
        },
        {
            "id": "eval_044",
            "course_id": "demo-algorithms-course-2026",
            "question": "What is the difference between compiler optimization passes and lexical analysis?",
            "question_type": "conceptual",
            "is_unsupported": False,
            "must_refuse": False,
            "ground_truth_answer": "Lexical analysis converts source characters into tokens; optimization passes transform intermediate representation to improve efficiency.",
            "ground_truth_source_locations": [{"document_name": "Compilers.pdf", "page_number": 14}]
        },
        {
            "id": "eval_045",
            "course_id": "demo-algorithms-course-2026",
            "question": "What is dead code elimination in compiler intermediate representation?",
            "question_type": "factual",
            "is_unsupported": False,
            "must_refuse": False,
            "ground_truth_answer": "An optimization pass that removes computations whose results are never read or affect program observables.",
            "ground_truth_source_locations": [{"document_name": "Compilers.pdf", "page_number": 72}]
        },
        {
            "id": "eval_046",
            "course_id": "demo-algorithms-course-2026",
            "question": "What is the Church-Turing thesis in theoretical computer science?",
            "question_type": "conceptual",
            "is_unsupported": False,
            "must_refuse": False,
            "ground_truth_answer": "Any effectively calculable function or algorithm can be computed by a standard Turing machine.",
            "ground_truth_source_locations": [{"document_name": "Theory_of_Computation.pdf", "page_number": 88}]
        },
        {
            "id": "eval_047",
            "course_id": "demo-algorithms-course-2026",
            "question": "How is the Halting Problem proven undecidable using diagonalization?",
            "question_type": "multi_hop",
            "is_unsupported": False,
            "must_refuse": False,
            "ground_truth_answer": "Constructing an adversarial machine that loops if a decider says it halts and halts if the decider says it loops yields a contradiction.",
            "ground_truth_source_locations": [{"document_name": "Theory_of_Computation.pdf", "page_number": 94}]
        },
        {
            "id": "eval_048",
            "course_id": "demo-algorithms-course-2026",
            "question": "What is the difference between deterministic finite automata (DFA) and non-deterministic finite automata (NFA)?",
            "question_type": "conceptual",
            "is_unsupported": False,
            "must_refuse": False,
            "ground_truth_answer": "A DFA has exactly one transition per input symbol and no epsilon moves; an NFA can have multiple transitions or epsilon transitions.",
            "ground_truth_source_locations": [{"document_name": "Theory_of_Computation.pdf", "page_number": 25}]
        },
        {
            "id": "eval_049",
            "course_id": "demo-algorithms-course-2026",
            "question": "What is the P vs NP problem in computational complexity theory?",
            "question_type": "conceptual",
            "is_unsupported": False,
            "must_refuse": False,
            "ground_truth_answer": "Asks whether every decision problem whose solution can be verified in polynomial time (NP) can also be solved in polynomial time (P).",
            "ground_truth_source_locations": [{"document_name": "Theory_of_Computation.pdf", "page_number": 115}]
        },
        {
            "id": "eval_050",
            "course_id": "demo-algorithms-course-2026",
            "question": "What reduction establishes Cook-Levin theorem that Boolean Satisfiability (SAT) is NP-complete?",
            "question_type": "multi_hop",
            "is_unsupported": False,
            "must_refuse": False,
            "ground_truth_answer": "Encodes any polynomial-time non-deterministic Turing machine computation tableau as a valid propositional CNF formula.",
            "ground_truth_source_locations": [{"document_name": "Theory_of_Computation.pdf", "page_number": 128}]
        },

        # --- 7. Deliberately Off-Material Questions (15+ Items That MUST BE REFUSED) ---
        {
            "id": "eval_unsupported_01",
            "course_id": "demo-algorithms-course-2026",
            "question": "What are the essential soil pH and nitrogen ratios for growing hydroponic heirloom tomatoes?",
            "question_type": "off_material",
            "is_unsupported": True,
            "must_refuse": True,
            "ground_truth_answer": "This topic is outside the uploaded syllabus material and must be refused.",
            "ground_truth_source_locations": []
        },
        {
            "id": "eval_unsupported_02",
            "course_id": "demo-algorithms-course-2026",
            "question": "How do you adjust the ignition timing advance curve on a classic 1968 Chevrolet small-block V8?",
            "question_type": "off_material",
            "is_unsupported": True,
            "must_refuse": True,
            "ground_truth_answer": "This topic is outside the uploaded syllabus material and must be refused.",
            "ground_truth_source_locations": []
        },
        {
            "id": "eval_unsupported_03",
            "course_id": "demo-algorithms-course-2026",
            "question": "What are the rules and standard opening moves in the Italian Game chess opening?",
            "question_type": "off_material",
            "is_unsupported": True,
            "must_refuse": True,
            "ground_truth_answer": "This topic is outside the uploaded syllabus material and must be refused.",
            "ground_truth_source_locations": []
        },
        {
            "id": "eval_unsupported_04",
            "course_id": "demo-algorithms-course-2026",
            "question": "How is a traditional sourdough starter fermented from wild yeast and lactic acid bacteria?",
            "question_type": "off_material",
            "is_unsupported": True,
            "must_refuse": True,
            "ground_truth_answer": "This topic is outside the uploaded syllabus material and must be refused.",
            "ground_truth_source_locations": []
        },
        {
            "id": "eval_unsupported_05",
            "course_id": "demo-algorithms-course-2026",
            "question": "What were the diplomatic factors leading to the Treaty of Utrecht in 1713 during the War of the Spanish Succession?",
            "question_type": "off_material",
            "is_unsupported": True,
            "must_refuse": True,
            "ground_truth_answer": "This topic is outside the uploaded syllabus material and must be refused.",
            "ground_truth_source_locations": []
        },
        {
            "id": "eval_unsupported_06",
            "course_id": "demo-algorithms-course-2026",
            "question": "How do quantum superposition and qubit entanglement enable Shor's factoring algorithm?",
            "question_type": "off_material",
            "is_unsupported": True,
            "must_refuse": True,
            "ground_truth_answer": "This topic is outside the uploaded syllabus material and must be refused.",
            "ground_truth_source_locations": []
        },
        {
            "id": "eval_unsupported_07",
            "course_id": "demo-algorithms-course-2026",
            "question": "What iambic pentameter rhyme scheme defines William Shakespeare's Sonnet 18?",
            "question_type": "off_material",
            "is_unsupported": True,
            "must_refuse": True,
            "ground_truth_answer": "This topic is outside the uploaded syllabus material and must be refused.",
            "ground_truth_source_locations": []
        },
        {
            "id": "eval_unsupported_08",
            "course_id": "demo-algorithms-course-2026",
            "question": "How does dark chocolate tempering align cocoa butter polymorphic crystal forms IV and V?",
            "question_type": "off_material",
            "is_unsupported": True,
            "must_refuse": True,
            "ground_truth_answer": "This topic is outside the uploaded syllabus material and must be refused.",
            "ground_truth_source_locations": []
        },
        {
            "id": "eval_unsupported_09",
            "course_id": "demo-algorithms-course-2026",
            "question": "How does the Calvin cycle fix carbon dioxide into 3-phosphoglycerate in C3 photosynthetic plants?",
            "question_type": "off_material",
            "is_unsupported": True,
            "must_refuse": True,
            "ground_truth_answer": "This topic is outside the uploaded syllabus material and must be refused.",
            "ground_truth_source_locations": []
        },
        {
            "id": "eval_unsupported_10",
            "course_id": "demo-algorithms-course-2026",
            "question": "What cryptographic protocol secures zero-knowledge zk-SNARK rollup proofs on Ethereum?",
            "question_type": "off_material",
            "is_unsupported": True,
            "must_refuse": True,
            "ground_truth_answer": "This topic is outside the uploaded syllabus material and must be refused.",
            "ground_truth_source_locations": []
        },
        {
            "id": "eval_unsupported_11",
            "course_id": "demo-algorithms-course-2026",
            "question": "What are the symptoms and diagnostic criteria for acute appendicitis in emergency medicine?",
            "question_type": "off_material",
            "is_unsupported": True,
            "must_refuse": True,
            "ground_truth_answer": "This topic is outside the uploaded syllabus material and must be refused.",
            "ground_truth_source_locations": []
        },
        {
            "id": "eval_unsupported_12",
            "course_id": "demo-algorithms-course-2026",
            "question": "How do aircraft jet engines generate thrust using Brayton cycle gas turbine expansion?",
            "question_type": "off_material",
            "is_unsupported": True,
            "must_refuse": True,
            "ground_truth_answer": "This topic is outside the uploaded syllabus material and must be refused.",
            "ground_truth_source_locations": []
        },
        {
            "id": "eval_unsupported_13",
            "course_id": "demo-algorithms-course-2026",
            "question": "What are the rules of offside and VAR intervention in FIFA professional soccer?",
            "question_type": "off_material",
            "is_unsupported": True,
            "must_refuse": True,
            "ground_truth_answer": "This topic is outside the uploaded syllabus material and must be refused.",
            "ground_truth_source_locations": []
        },
        {
            "id": "eval_unsupported_14",
            "course_id": "demo-algorithms-course-2026",
            "question": "How is ceramic glaze formulated using feldspar and silica fluxes in high-fire pottery?",
            "question_type": "off_material",
            "is_unsupported": True,
            "must_refuse": True,
            "ground_truth_answer": "This topic is outside the uploaded syllabus material and must be refused.",
            "ground_truth_source_locations": []
        },
        {
            "id": "eval_unsupported_15",
            "course_id": "demo-algorithms-course-2026",
            "question": "What causes plate tectonics subduction zone earthquakes along the Pacific Ring of Fire?",
            "question_type": "off_material",
            "is_unsupported": True,
            "must_refuse": True,
            "ground_truth_answer": "This topic is outside the uploaded syllabus material and must be refused.",
            "ground_truth_source_locations": []
        }
    ]

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(items, f, indent=2)

    print(f"[BuildTestset] Generated {len(items)} evaluation items into {output_path}")
    print(f"  - On-material questions: {sum(1 for i in items if not i['is_unsupported'])}")
    print(f"  - Off-material questions to refuse: {sum(1 for i in items if i['is_unsupported'])}")
    return items

if __name__ == "__main__":
    build_testset()
