import os
import pymupdf as fitz
from pptx import Presentation
from pptx.util import Inches, Pt
import cv2
import numpy as np

def generate_demo_course_materials():
    materials_dir = os.path.join(os.path.dirname(__file__), "..", "..", "data", "demo_materials")
    os.makedirs(materials_dir, exist_ok=True)

    pdf_path = os.path.join(materials_dir, "chapter_algorithms.pdf")
    pptx_path = os.path.join(materials_dir, "lecture_dynamic_programming.pptx")
    video_path = os.path.join(materials_dir, "lecture_video_transcript.mp4")

    # 1. Create chapter_algorithms.pdf
    doc = fitz.open()

    # Page 1: Foundations & Asymptotic Analysis
    p1 = doc.new_page(width=612, height=792)
    p1.insert_text((50, 60), "Design and Analysis of Algorithms", fontsize=18)
    p1.insert_text((50, 85), "Chapter 1: Foundations and Asymptotic Complexity", fontsize=14)
    p1.insert_text((50, 120), "1.1 Asymptotic Analysis and Big-O Notation", fontsize=12)
    text_p1 = (
        "Asymptotic analysis evaluates algorithm performance as input size grows toward infinity.\n"
        "Big-O notation represents an asymptotic upper bound: f(n) = O(g(n)) if there exist positive constants c and n0 such that 0 <= f(n) <= c*g(n) for all n >= n0.\n"
        "Omega notation represents an asymptotic lower bound, providing a guaranteed minimum growth rate.\n"
        "Theta notation represents an asymptotically tight bound, holding when an algorithm matches both its upper and lower bounds.\n"
        "Analyzing growth rates allows engineers to compare algorithmic efficiency independently of hardware differences."
    )
    p1.insert_textbox(fitz.Rect(50, 135, 550, 320), text_p1, fontsize=10)

    p1.insert_text((50, 340), "1.2 Recurrence Relations and Divide and Conquer", fontsize=12)
    text_p1_2 = (
        "Divide and conquer algorithms partition a problem into smaller independent subproblems, solve each subproblem recursively, and combine their solutions.\n"
        "Merge Sort divides an array of size n into two halves, sorts each half recursively, and merges the sorted halves in linear time.\n"
        "The governing recurrence relation is T(n) = 2T(n/2) + O(n).\n"
        "Base case formulation occurs when n <= 1, where sorting takes constant O(1) operations.\n"
        "Solving this recurrence yields an optimal worst-case time complexity of O(n log n)."
    )
    p1.insert_textbox(fitz.Rect(50, 355, 550, 520), text_p1_2, fontsize=10)

    # Draw diagram box on Page 1
    shape = p1.new_shape()
    shape.draw_rect(fitz.Rect(50, 540, 550, 700))
    shape.finish(color=(0.2, 0.4, 0.6), fill=(0.95, 0.97, 1.0))
    shape.commit()
    p1.insert_text((70, 565), "Figure 1.1: Recurrence Tree for Divide and Conquer Merge Sort", fontsize=11)
    p1.insert_text((70, 595), "Level 0:  T(n)                             Cost: cn", fontsize=9)
    p1.insert_text((70, 620), "Level 1:  T(n/2)        T(n/2)             Cost: cn", fontsize=9)
    p1.insert_text((70, 645), "Level 2:  T(n/4) T(n/4) T(n/4) T(n/4)      Cost: cn", fontsize=9)
    p1.insert_text((70, 670), "Total Tree Height: log2(n)   |   Overall Sum: O(n log n)", fontsize=9)

    # Page 2: Master Theorem & Dynamic Programming
    p2 = doc.new_page(width=612, height=792)
    p2.insert_text((50, 60), "1.3 Master Theorem and Recurrence Trees", fontsize=12)
    text_p2 = (
        "The Master Theorem provides a cookbook solution for recurrences of the form T(n) = aT(n/b) + f(n), where a >= 1 and b > 1.\n"
        "Case 1 applies when f(n) is polynomially smaller than n^(log_b a), yielding T(n) = Theta(n^(log_b a)).\n"
        "Case 2 applies when f(n) and n^(log_b a) are asymptotically equal, yielding T(n) = Theta(n^(log_b a) * log n).\n"
        "Case 3 applies when f(n) is polynomially larger, yielding T(n) = Theta(f(n))."
    )
    p2.insert_textbox(fitz.Rect(50, 75, 550, 220), text_p2, fontsize=10)

    p2.insert_text((50, 240), "1.4 Dynamic Programming Foundations", fontsize=12)
    text_p2_2 = (
        "Dynamic Programming is an algorithmic technique for solving optimization problems by breaking them down into overlapping subproblems.\n"
        "Optimal substructure means that an optimal solution to the problem contains within its structure optimal solutions to subproblems.\n"
        "This property is an indispensable requirement for both dynamic programming and greedy algorithms.\n"
        "Overlapping subproblems means that a recursive formulation visits the same subproblems repeatedly rather than generating new subproblems.\n"
        "Memoization maintains a top-down lookup table so each subproblem state is calculated at most once.\n"
        "Tabulation is a bottom-up iterative approach, systematically populating an array from the base cases upward to avoid recursion overhead."
    )
    p2.insert_textbox(fitz.Rect(50, 255, 550, 440), text_p2_2, fontsize=10)

    p2.insert_text((50, 460), "1.5 The 0/1 Knapsack Problem", fontsize=12)
    text_p2_3 = (
        "The 0/1 Knapsack problem considers n items, each with weight w_i and value v_i, and a knapsack with maximum weight capacity W.\n"
        "The state definition is dp[i][w], representing the maximum value achievable considering a subset of the first i items with capacity at most w.\n"
        "The state transition equation is:\n"
        "dp[i][w] = max(dp[i-1][w], dp[i-1][w - w_i] + v_i) when w_i <= w.\n"
        "If the item exceeds available capacity, we inherit dp[i][w] = dp[i-1][w].\n"
        "The running time complexity is O(n * W), which is pseudo-polynomial because W is represented in log(W) input bits."
    )
    p2.insert_textbox(fitz.Rect(50, 475, 550, 680), text_p2_3, fontsize=10)

    # Page 3: Graph Traversal & Shortest Paths
    p3 = doc.new_page(width=612, height=792)
    p3.insert_text((50, 60), "1.6 Graph Algorithms and Shortest Paths", fontsize=12)
    text_p3 = (
        "Graph algorithms operate on collections of vertices V and edges E.\n"
        "Breadth-First Search (BFS) explores all neighboring vertices at the current depth before advancing, finding shortest unweighted paths.\n"
        "Depth-First Search (DFS) systematically progresses along each branch before backtracking, establishing discovery and finish timestamps.\n"
        "Topological Sort produces a linear ordering of vertices in a Directed Acyclic Graph (DAG) such that for every directed edge u -> v, u appears before v.\n"
        "Dijkstra Algorithm computes the single-source shortest path in graphs with non-negative edge weights using a priority queue.\n"
        "Bellman-Ford Algorithm computes shortest paths in graphs with arbitrary edge weights and detects negative weight cycles in O(V * E) time."
    )
    p3.insert_textbox(fitz.Rect(50, 75, 550, 300), text_p3, fontsize=10)

    doc.save(pdf_path)
    doc.close()

    # 2. Create lecture_dynamic_programming.pptx
    prs = Presentation()
    prs.slide_width = Inches(10)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    slides_content = [
        ("Dynamic Programming and Optimal Substructure", [
            "Course: Design and Analysis of Algorithms",
            "Unit 4: Advanced Dynamic Programming & State Space Optimization",
            "Instructor Lecture Series • Academic Year 2026"
        ]),
        ("Optimal Substructure Definition", [
            "Formal Condition: An optimal solution to a problem contains optimal solutions to its subproblems.",
            "Shortest Path Property: If path P from u to v is shortest, any sub-path from x to y on P is also shortest.",
            "Indispensable Foundation: Required for both dynamic programming and greedy algorithms."
        ]),
        ("Overlapping Subproblems", [
            "Distinction from Divide-and-Conquer: Subproblems are shared across branches rather than disjoint.",
            "Fibonacci Recurrence: Naive recursion computes F(n-2) exponentially many times (O(2^n)).",
            "State Space Caching: Evaluates each unique state exactly once, reducing complexity to polynomial time."
        ]),
        ("Top-Down Memoization vs Bottom-Up Tabulation", [
            "Memoization: Top-down recursive evaluation maintaining a cache dictionary or lookup array.",
            "Tabulation: Bottom-up iterative table filling from base cases upward to avoid call-stack overhead.",
            "Trade-off: Memoization computes only reachable states; tabulation provides better cache locality."
        ]),
        ("0/1 Knapsack State Space Formulation", [
            "Problem Formulation: Given n items with weights w_i and values v_i, capacity W.",
            "State Definition: dp[i][w] = maximum value using items 1..i within weight capacity w.",
            "Recurrence: dp[i][w] = max(dp[i-1][w], dp[i-1][w - w_i] + v_i) for w >= w_i.",
            "Complexity: O(n * W) time and O(n * W) space, pseudo-polynomial time complexity."
        ]),
        ("Dijkstra Algorithm and Shortest Paths", [
            "Single-source shortest paths on weighted graphs with non-negative edge weights.",
            "Greedy Invariant: Maintains set of visited vertices whose shortest distance is permanently finalized.",
            "Priority Queue Implementation: Min-heap yields O((V + E) log V) time complexity."
        ])
    ]

    for title, bullets in slides_content:
        s = prs.slides.add_slide(blank_layout)
        tx_box = s.shapes.add_textbox(Inches(0.8), Inches(0.8), Inches(8.4), Inches(1.2))
        tf = tx_box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(24)
        p.font.bold = True

        b_box = s.shapes.add_textbox(Inches(0.8), Inches(2.2), Inches(8.4), Inches(4.5))
        btf = b_box.text_frame
        btf.word_wrap = True
        for idx, b_text in enumerate(bullets):
            bp = btf.paragraphs[0] if idx == 0 else btf.add_paragraph()
            bp.text = "• " + b_text
            bp.font.size = Pt(15)
            bp.space_after = Pt(12)

    prs.save(pptx_path)

    # 3. Create lecture_video_transcript.mp4
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(video_path, fourcc, 2.0, (640, 480))
    for i in range(10):
        frame = np.zeros((480, 640, 3), dtype=np.uint8)
        frame[:] = (30, 40, 50)
        cv2.putText(frame, "Algorithms Lecture 4: Dynamic Programming", (40, 240), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        out.write(frame)
    out.release()

    return {
        "pdf_path": pdf_path,
        "pptx_path": pptx_path,
        "video_path": video_path
    }

if __name__ == "__main__":
    res = generate_demo_course_materials()
    print("Generated demo course materials:", res)
