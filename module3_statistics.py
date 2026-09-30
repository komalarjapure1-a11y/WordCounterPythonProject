import matplotlib.pyplot as plt


# =========================================================
# MODULE 3: FREQUENCY ANALYSIS & VISUALIZATION
# =========================================================

def show_graph(frequency):

    top_words = frequency.most_common(10)

    word_names = []
    word_counts = []

    for word, count in top_words:
        word_names.append(word)
        word_counts.append(count)

    # Create graph
    plt.figure(
        figsize=(10, 5)
    )

    bars = plt.bar(
        word_names,
        word_counts
    )

    plt.xlabel(
        "Words",
        fontsize=12
    )

    plt.ylabel(
        "Frequency",
        fontsize=12
    )

    plt.title(
        "Top 10 Most Frequently Used Words",
        fontsize=15,
        fontweight="bold"
    )

    plt.xticks(
        rotation=45
    )

    # Display values above bars
    for bar in bars:
        height = bar.get_height()

        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            str(int(height)),
            ha="center",
            va="bottom"
        )

    plt.tight_layout()

    plt.show()