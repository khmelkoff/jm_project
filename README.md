# GraphRAG + Ollama + Cyberpunk

Project folder with the results of the experiments

## Getting started

for reference: https://microsoft.github.io/graphrag/get_started/

1. conda create --name jm_project python==3.11
2. conda activate jm_project
3. cd <project_folder_path>
4. check settings.yaml api_base and vector_size params
5. install requirements for embedding_proxy:
    - install torch with or without cuda support, https://pytorch.org/get-started/locally/
    - for example: pip install torch --index-url https://download.pytorch.org/whl/cu126
    - install other requirements: pip install -r requirements.txt
6. pull the model (qwen3:14b)
7. start embedding_proxy: python embedding_proxy.py --port 11435
8. stop Ollama if running and set env. variables:
    - set OLLAMA_HOST=0.0.0.0:11434 (if the ollama on the another machine)
    - set OLLAMA_CONTEXT_LENGTH=12288
    - start ollama: ollama serve

## Query

### Global query
```console
graphrag query "What are the top cyberpunk elements in this story?"
```
example response:

#### Key Cyberpunk Elements in the Story

The narrative prominently features several quintessential cyberpunk elements, each underscored by specific technological, societal, and thematic motifs. These elements collectively paint a picture of a dystopian, high-tech, and morally ambiguous world. Below is a synthesis of the most salient aspects derived from the dataset.

##### **Technological Augmentation and Neural Manipulation**
Cybernetic enhancements and neural technology are central to the story’s setting. Characters such as Lewis employ **neural disruptors**, devices that align with cyberpunk themes of **technological augmentation and mind-control-related technology** [Data: Reports (2, 10, 19, 25, +more)]. Similarly, the Yakuza’s use of a **prosthetic thumb** exemplifies the fusion of human and machine, a hallmark of cyberpunk narratives where organic and synthetic elements coexist [Data: Reports (10, 19, 25, +more)]. These technologies not only highlight the pervasive influence of advanced machinery on human physiology but also raise ethical questions about autonomy and control.

##### **Gritty Urban Environments and Lawlessness**
The story’s urban landscapes are defined by **dystopian decay and high-stakes chaos**. The **Drome** functions as a central hub for **business, criminal, and law enforcement activities**, encapsulating the gritty, high-stakes atmosphere typical of cyberpunk settings [Data: Reports (2)]. Similarly, **Nighttown** is portrayed as a **lawless, decaying district** marked by surrealism and societal fragmentation, embodying the cyberpunk trope of a **fractured, chaotic society** [Data: Reports (29, 30, 39, +more)]. These environments reflect a world where order is tenuous, and power is concentrated in the hands of a few, leaving the marginalized to navigate a treacherous existence.

##### **Dominance of Megacorporations and Criminal Syndicates**
Power structures in the story are dominated by **megacorporations and organized crime syndicates**, such as the **Yakuza**, which engage in **illicit activities and corporate programs** [Data: Reports (2, 15, 25, +more)]. These entities operate with impunity, often blurring the lines between legal and illegal enterprises. The Yakuza’s role as **enforcers for illicit operations** [Data: Reports (2)] further underscores the intersection of **corporate and criminal power structures**, a defining feature of cyberpunk worldbuilding. This dynamic highlights the systemic corruption and the erosion of state authority in favor of private, profit-driven interests.

##### **Decommissioned Technology and Reuse**
The narrative also explores the **decay and repurposing of technology**, a recurring theme in cyberpunk fiction. **Derelict sites** such as the **FUNLAND amusement park**, featuring **JONES’s seawater tank**, and the **Killing Floor**, which hosts **combat events**, illustrate how **outdated technology is repurposed or abandoned** [Data: Reports (31, 43, 47, +more)]. These settings symbolize the **ephemeral nature of technological progress** and the **inevitable obsolescence** of even the most advanced systems, often left to languish in decay or co-opted for new, often violent, purposes.

##### **Surveillance, Hacking, and Data Manipulation**
The story incorporates themes of **surveillance and data control**, with characters like **JONES** possessing **data-tracking abilities** that imply **hacking and manipulation of information** [Data: Reports (47, 25, 50, +more)]. The Yakuza’s concerns about **evidence exposure via neural interfaces** further emphasize the **permeability of digital and physical realms**, a cornerstone of cyberpunk narratives. These elements reflect a world where **privacy is eroded**, and **information is both a weapon and a commodity**, often manipulated by those in power to maintain control.

##### **Rogue Agents and Mercenaries**
Characters such as **Molly Millions** embody the **rogue agent archetype**, operating as **technologically savvy mercenaries** who leverage skills in **combat, negotiation, and control unit extraction** [Data: Reports (2)]. Her presence underscores the **ubiquity of mercenaries and hackers** in cyberpunk settings, where **individuals with specialized skills** often navigate a **lawless, corporate-dominated world**. Similarly, the **Magnetic Dog Sisters**, described as **enforcers with martial arts expertise**, contribute to the **physically imposing, heavily armed characters** that populate cyberpunk narratives, reinforcing the genre’s focus on **violence and power imbalances** [Data: Reports (2)].

#### Implications and Thematic Resonance
These elements collectively reinforce the **core tenets of cyberpunk fiction**: the **clash between humanity and technology**, the **corruption of societal institutions**, and the **resilience of marginalized individuals**. The **fusion of organic and synthetic elements** (e.g., neural disruptors, prosthetics) raises existential questions about **identity and autonomy**, while the **dominance of megacorporations** critiques **capitalism’s unchecked expansion**. The **lawless urban environments** and **repurposed technology** serve as metaphors for **societal decay and the cyclical nature of progress**. Meanwhile, the **presence of rogue agents and mercenaries** highlights the **fragmentation of loyalty and the moral ambiguity** that defines the genre.

In summary, the story’s cyberpunk elements are not merely aesthetic choices but **narrative tools** that interrogate the **consequences of technological advancement, the erosion of privacy, and the power dynamics** between individuals and institutions. These themes are woven into the fabric of the dataset, offering a rich tapestry of **speculative fiction** that resonates with the **social and philosophical concerns** of the cyberpunk genre.

### Local query
```console
graphrag query "Who is JONES and what are his main relationships?" -m local
```
example response:

Jones is a cyborg dolphin with advanced sensory capabilities, prominently featured in the narrative as a key figure within Funland, a derelict amusement park and zoo. His role involves managing a tank filled with fresh seawater and collaborating with a Squid, which reads traces of data or information [Data: Entities (28), Relationships (47, +more)]. Jones is also deeply involved in a data retrieval operation with Molly Millions and Johnny, where his unique physiology allows him to access data from Johnny’s chip, highlighting his technological prowess and significance in high-stakes scenarios [Data: Entities (33), Relationships (44, 51, 54, +more)].

Jones’s connection to Funland is central to his identity, as described in the narrative. Funland is depicted as a liminal space, blending elements of a derelict zoo with technological and cybernetic elements. Jones’s presence there underscores his ambiguous status—whether as an operator, detainee, or something in between—adding layers of complexity to his character [Data: Entities (28), Sources (3)]. His interactions with Molly and Johnny further emphasize his role as a pivotal figure navigating both cooperative and adversarial dynamics within the community.

Jones’s relationships extend beyond Funland and the data retrieval operation. His association with the Squid, a device linked to the Yakuza’s concerns about evidence and program traces, suggests a broader involvement in the narrative’s themes of surveillance, data, and conflict [Data: Entities (19), Relationships (25, +more)]. While his exact status and the full extent of his activities remain partially unresolved, his contributions to the community’s complexity and narrative depth are undeniable, positioning him as a multifaceted entity at the intersection of technology, performance, and subversion [Data: Sources (3), Relationships (47, 44, +more)].
    