# Writing style guide — Albert's voice (thesis prose)

**Created:** Oct 1, 2026 (orchestration session) · **Approved by Albert:** Oct 1, 2026
**Derived from three of Albert's own texts** (not in the repo):
- the essay on water management in the semiconductor supply chain (single author);
- *Artificial Intelligence Implementation in Customer Service* (single author);
- the HP case report (Group 21; used with less weight).

**Applies to:** every chapter draft and every writing brief from now on. It sits on top of the existing source and argument rules (verified sources, quotes checked against PDFs, Presc./Obs. distinction, no interview data, no organisation names), which it never overrides.

## 1. What this voice does

1. **It signposts, then walks through.** Announce the structure, then follow it.
   - *"I believe there are three primary reasons why AI chatbots cannot fully replace human agents: training issues, negative experiences, and concerns about losing the ability to choose."*
   - *"The first reason is… Secondly… Finally…"*; *"Action 1 … Action 5"*; *"To sum up my suggestions…"*

   In the thesis: open a section or a long paragraph with what it will show ("This section sets out three…"; "Two points follow from this."), then use **First / Second / Finally** or **The first … The second …**.
2. **It states the author's position plainly**, sparingly and at the point of argument.
   - *"In my view…"*, *"I believe…"*, *"we argue…"*
   - Thesis rule (decision **B**, Oct 1): in Chapters 1–2, use **"I argue that…"**, **"In my view…"** or **"I suggest…"** at key claims, **one to three times per section**. Use them where a claim is the author's reading of the literature, not a report of a source. Default subject otherwise: "this study". Chapter 3 keeps "I" for researcher decisions.
3. **It carries logic with explicit connectors:** *However, Furthermore, Moreover, In addition, Thus, Therefore, Hence, For example, For instance, In contrast, As a result, In other words, In conclusion, To sum up.* Prefer a connector to a colon or a semicolon when the link is causal or contrastive.
4. **It goes from concrete to abstract.** A trend or a dated event first ("after ChatGPT was released in 2022…"), then a number or a case with its source, then the point drawn from it ("Thus…", "This shows…").
5. **It uses moderate, direct sentences.** One main idea per sentence; split sentences joined by semicolons or chains of colons. Plain verbs (*shows, finds, argues, suggests, describes*), not compressed nominalisations.
6. **Its headings say what the section argues or does.** Keep the thesis headings (questions in Ch2, topics in Ch1/Ch3). Within a section, the first sentence states the point.
7. **It closes with a summary.** End a section with one or two plain sentences that sum up ("In short…", "To sum up…", "Therefore…"), not with an aphorism.

## 2. What to avoid (drift seen in the earlier drafts)

- **Aphoristic closers and inverted rhetoric**, e.g. *"The analyst who used to write an analysis now has to audit one they did not write."* → *"In other words, analysts no longer only write the analysis; they also have to check an analysis that they did not write."*
- **Long sentences held together by colons and semicolons.** Split them and add a connector.
- **Over-compressed abstraction**, e.g. "a rule's effect is settled where it is received". Say it plainly: "whether a rule works is decided at the point where someone receives it".
- **More than two em dashes per page** (unchanged rule); the AI-typical word list (unchanged).

## 3. What not to copy from the source texts

- **Grammar slips in the old papers.** For example *"My imagine to AI customer service"*, *"water force diversity"*, missing articles, *"Reason of…"*. The thesis keeps correct academic English and UK spelling.
- **Loose citation forms** ("(Chen. H, 2006)"). Keep pandoc `[@key, p. N]` and APA 7.
- **Recommendation framing** ("Nvidia should…"). The thesis analyses; it does not advise, except in Chapter 6.

## 4. What a style pass must never change

- Quotes, page numbers, citation keys, the facts a sentence claims, and the strength of a claim. "Describe" does not become "argue"; "may" does not become "will".
- **Key terms:** *BI practitioners, rule, ruling, working rule, carriers / recipients, prescribed / observed, intermediary, depth / breadth case*, the R1 coding rule.
- **Text fixed word for word:** RQ v2.1 and the BI practitioner definition (1.4 ¶4 = 3.2 ¶1).
- `[PENDING]`, `[FILL]` and `[CHECK]` markers.
- Section and paragraph structure. Word count stays within ±10% of the section target.

**Check after every style pass:** re-run the quote check against the PDFs. Every quoted string must still be present and on the same page.

## 5. Before / after example (1.1 ¶3)

**Before:** "Generative AI (GenAI) changes what this work involves. … The new task is not easy: existing assistants offer little support for verification, and "even experts can be susceptible…" … The analyst who used to write an analysis now has to audit one they did not write."

**After:** "However, generative AI (GenAI) is changing what this work involves. For example, … This new task is not easy. Existing assistants offer little support for verification, and "even experts can be susceptible…" … In other words, analysts no longer only write the analysis; they also have to check an analysis that they did not write."
