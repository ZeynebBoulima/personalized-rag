# Semantic Chunking

## Purpose

The chunking module divides a document into coherent semantic units.

Instead of splitting text by a fixed number of characters, it attempts to preserve the meaning of the document.

---

## Why semantic chunking?

Fixed-size chunking is simple but introduces several problems.

- Sentences may be cut in half.
- Related ideas may be separated.
- Retrieval quality decreases.

Semantic chunking groups together sentences that discuss the same topic.

---

## Initial approach

The first implementation compared every sentence with the following sentence using cosine similarity.

Sentence i
        ↓
Sentence i + 1

If similarity was below a threshold, a new chunk was created.

Although functional, this approach produced excessive fragmentation because every decision depended only on two neighboring sentences.

---

## Current approach

The current implementation builds chunks incrementally.

Each chunk maintains a centroid representing the average semantic meaning of all its sentences.

For every new sentence:

1. Generate its embedding.
2. Compare it to the current chunk centroid.
3. If similarity is above the threshold:
   - add the sentence
   - update the centroid
4. Otherwise:
   - finalize the current chunk
   - start a new one

This approach considers the entire topic represented by the chunk instead of only the previous sentence.

---

## Advantages

- Better topic coherence
- More stable chunk boundaries
- Reduced over-segmentation
- Easier to extend

---

## Future improvements

- Dynamic similarity threshold
- Sliding-window centroid
- Maximum chunk size
- Overlapping chunks
- Hierarchical chunking