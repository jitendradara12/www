+++
date = '2026-03-29T16:54:05+05:30'
title = 'COA'
+++

> ##### !NOTE
>
> This is Slop

##### CHAPTER 5

---

## 1. Memory & Bit Math (The "Instruction Format" Hack)

When a question asks you to calculate bits for memory, addresses, or registers, use these unbreakable rules:

- **Rule of Memory Size (`N`):** If memory has `N` words, you need `k` bits for the address, where `2^k = N`.
  > _Exam Trick:_ If memory is `256K`, break it down: `256 * 1024 = 2^8 * 2^{10} = 2^{18}`. You need **18 bits** for the address.
- **The Data Bus:** Data bus size = the size of exactly **one word** (e.g., if memory is 256K words of 32 bits, the data bus is 32 bits).
- **The Address Bus:** Address bus size = the number of bits needed to address memory (e.g., 18 bits from the example above).
- **Register Bits:** If you have `R` registers, you need `n` bits to select one, where `2^n = R` (e.g., 64 registers = `2^6 -> 6` bits).

### The Anatomy of an Instruction Word

Total Bits = `[Indirect Bit (I)]` + `[Opcode]` + `[Register Code (if any)]` + `[Address]`

---

## 2. Decoding the Matrix: Hex to Instruction Type

For tracing questions, you are often given a 4-digit Hex instruction (like `932E`). The **first hex digit** is the master key. It contains the Indirect bit (`I`) AND the 3-bit Opcode.

Convert that first hex digit into 4-bit binary `->` `[ I | Opcode (3 bits) ]`

| First Hex Digit | `I` Bit |     Opcode     | Instruction Category     | What does it mean?                                                   |
| :-------------- | :-----: | :------------: | :----------------------- | :------------------------------------------------------------------- |
| **0 to 6**      |   `0`   | `000` to `110` | **Direct** Memory Ref.   | The address part _is_ the actual location of the data.               |
| **8 to E**      |   `1`   | `000` to `110` | **Indirect** Memory Ref. | The address part points to a location that _holds_ the real address. |
| **7**           |   `0`   |     `111`      | **Register** Reference   | Math/Logic on registers (e.g., CLA, CMA). No memory access.          |
| **F**           |   `1`   |     `111`      | **I/O** Reference        | Input/Output commands.                                               |

---

## 3. The Register Roster (Who does what?)

To fill out trace tables accurately, you must know what each register holds:

- **PC (Program Counter):** Holds the address of the _next_ instruction to be read.
- **AR (Address Register):** Points to the specific memory location being read/written _right now_.
- **IR (Instruction Register):** Holds the actual instruction currently being executed.
- **DR (Data Register):** Holds the operand (data) read from memory.
- **AC (Accumulator):** The main workspace. All math and logic happen here.

---

## 4. The Heartbeat: The Instruction Cycle (`T_0` to `T_3`)

Every single instruction goes through these exact phases. Memorize this sequence for your trace tables.

1.  **Fetch Phase (`T_0, T_1`):** Go get the instruction.
    - `T_0`: `AR <- PC` _(Tell memory where to look)_
    - `T_1`: `IR <- M[AR]`, `PC <- PC + 1` _(Bring instruction into IR, increment PC)_
2.  **Decode Phase (`T_2`):** Figure out what the instruction is.
    - `T_2`: Decode Opcode in IR, send the address part to AR (`AR <- IR(0-11)`), extract the `I` bit.
3.  **Indirect Phase (`T_3`):** _(Only happens if `I=1` and it's a Memory Reference instruction)._
    - `T_3`: `AR <- M[AR]` _(Go to memory, get the real address, put it in AR)._
4.  **Execute Phase (`T_4, T_5 ...`):** Do the math or data movement (see Section 5).

---

## 5. Memory-Reference Instructions (The "Big 7")

When decoding Opcodes `0` to `6`, here is exactly what happens during the Execute phase. **Pay close attention to the "What Changes" column for your trace tables!**

| Opcode | Mnemonic | Name                | The Execution Logic (`T_4, T_5`)                                             | What Changes?                 |
| :----: | :------- | :------------------ | :--------------------------------------------------------------------------- | :---------------------------- |
|  `0`   | **AND**  | AND to AC           | `DR <- M[AR]` <br> `AC <- AC & DR`                                           | **AC**                        |
|  `1`   | **ADD**  | Add to AC           | `DR <- M[AR]` <br> `AC <- AC + DR`                                           | **AC**                        |
|  `2`   | **LDA**  | Load AC             | `DR <- M[AR]` <br> `AC <- DR`                                                | **AC**                        |
|  `3`   | **STA**  | Store AC            | `M[AR] <- AC`                                                                | **Memory!** (AC is untouched) |
|  `4`   | **BUN**  | Branch Uncond.      | `PC <- AR`                                                                   | **PC**                        |
|  `5`   | **BSA**  | Branch & Save       | `M[AR] <- PC` <br> `PC <- AR + 1`                                            | **Memory, PC**                |
|  `6`   | **ISZ**  | Inc. & Skip if Zero | `DR <- M[AR] + 1` <br> `M[AR] <- DR` <br> If (`DR == 0`) then `PC <- PC + 1` | **Memory**, (maybe PC)        |

---

## 6. Exam Strategy: How to Dominate Trace Tables

When faced with a question like Tutorial Q4 (showing contents of PC, IR, AC, DR, AR after execution), run this loop in your head:

1.  **Start:** Look at the initial PC. Look up that address in memory to find your instruction.
2.  **Fetch:** Write down the new PC (`PC + 1`). Put the memory contents into the **IR**. Put the last 3 hex digits of the instruction into the **AR**.
3.  **Decode/Indirect:** Look at the first hex digit in the IR. If it's an Indirect instruction (8-E), you must go to memory at the address in AR, read the value there, and update AR with _that_ new value.
4.  **Execute:** Apply the logic from the "Big 7" table above. Update the AC, DR, or Memory.
5.  **Record:** Fill in your table row with the _final_ states of all registers after execution.
6.  **Loop:** Look at your current PC. That's your next instruction. Rinse and repeat until you hit a `HLT` (halt) command.

##### CHAPTER 6 (Programming the Basic Computer )

---

## 1. Machine vs. Assembly Language

- **Machine Language:** The raw binary (1s and 0s) the hardware actually executes. Tied directly to the 16-bit instruction format.
- **Assembly Language:** The human-readable version.
- **The Golden Rule:** 1 Assembly Instruction = 1 Machine Instruction (usually 1 memory word).

## 2. Assembly Language Rules

An assembly line has three distinct fields:

1.  **Label:** (Optional) Marks a memory address. Ends with a comma (e.g., `L1,`).
2.  **Instruction:** The Opcode (e.g., `ADD`, `LDA`) + Address/Register + Mode (`I` for indirect).
3.  **Comment:** (Optional) Starts with a slash `/`.

**Pseudoinstructions** (Exam Trap!): These do _not_ translate to machine code. They tell the assembler what to do.

- `ORG N`: Sets the Location Counter (LC) to Hex address `N`.
- `END`: Tells the assembler to stop.
- `DEC N` / `HEX N`: Stores a decimal/hex constant in memory.

## 3. Exam Hack: Translation to Binary (Pass 1 & Pass 2)

_If a question asks you to convert an Assembly program to Hex/Binary, follow these exact steps:_

**Pass 1: Build the Address Symbol Table (AST)**
You need to know where every label lives in memory.

1.  Look at the first `ORG` directive to set your starting Location Counter (LC).
2.  Go line by line. Increment the LC by 1 for each line.
3.  If you see a Label, write down the Label and the current LC value. _Ignore the actual instructions for now._

**Pass 2: Translate to Hex**

1.  Look up the Opcode in your Mano reference table (e.g., direct `LDA` = `2`, indirect `LDA I` = `A`).
2.  If the instruction has a Label as its address, replace it with the hex address you found in your AST during Pass 1.
3.  Combine the Opcode (1 hex digit) and Address (3 hex digits) to form the 4-digit Hex instruction.
4.  _Binary Translation:_ Expand each hex digit into 4 bits.

> 💡 **Tracking Registers (AC, PC, IR):**
>
> - **PC (Program Counter):** Always holds the address of the _next_ instruction. After fetching an instruction at address `100`, PC becomes `101`.
> - **IR (Instruction Register):** Holds the exact 16-bit binary/hex of the instruction currently executing.
> - **AC (Accumulator):** Holds the math/logic result after the execution phase.

##### CHAPTER 8 (Central Processing Unit)

---

## 1. General Register Organization & The Bus

Instead of connecting every register to every other register, CPUs use a **Common Bus** system.

- **MUX A & MUX B:** Select two source registers to send data _into_ the ALU.
- **ALU (Arithmetic Logic Unit):** Performs the operation.
- **Decoder:** Selects which destination register receives the data _from_ the ALU.

## 2. Exam Hack: Calculating Hardware Bit Sizes

_Word problems will give you `R` (number of registers) and `O` (number of ALU operations). Here is how you size the hardware:_

1.  **Multiplexer Size:** You have `R` registers. You also need 1 external input port.
    - _Total Inputs_ = `R + 1`.
    - _Size_ = Find the next power of 2. (e.g., 15 registers + 1 external = 16 inputs. Size is `16 * 1` MUX).
2.  **Selection Lines (Control Bits):** \* If MUX inputs = `2^k`, you need `k` selection lines. (e.g., for 16 inputs, `2^4 = 16`, so `k = 4` bits).
3.  **Decoder Size:** \* Takes the destination bits and decodes them to load one register.
    - _Size_ = `k * (R+1)`. (e.g., a `4 * 16` decoder).
4.  **ALU OPR Bits:**
    - If the ALU has `N` operations, find the next power of 2: `2^m >= N`.
    - `m` is the number of bits needed for the OPR field. (e.g., 35 operations requires 64 slots `-> 2^6`, so `m=6` bits).

## 3. The Control Word

The CPU is controlled by a binary word that dictates exactly what the Bus and ALU do in one clock cycle.

| SELA (Source A) | SELB (Source B) | SELD (Destination) | OPR (Operation) |
| :-------------- | :-------------- | :----------------- | :-------------- |
| `k` bits        | `k` bits        | `k` bits           | `m` bits        |

**Microoperation Example:** `R1 <- R2 + R3`

- **SELA:** Code for `R2`
- **SELB:** Code for `R3`
- **SELD:** Code for `R1`
- **OPR:** Code for `ADD`

---

# Bonus Logic Toolbox (For Bit Manipulation Questions)

If an exam question asks you to modify specific bits in a 16-bit value without touching the others, use these masks:

| Goal                  | Logic Operation | Mask Needed                         | Intuition                        |
| :-------------------- | :-------------- | :---------------------------------- | :------------------------------- |
| **Clear** bits to 0   | **AND**         | `0` for target bits, `1` for others | `X AND 0 = 0`, `X AND 1 = X`     |
| **Set** bits to 1     | **OR**          | `1` for target bits, `0` for others | `X OR 1 = 1`, `X OR 0 = X`       |
| **Complement** (Flip) | **XOR**         | `1` for target bits, `0` for others | `X XOR 1 = NOT X`, `X XOR 0 = X` |

_Example:_ To clear the 8 Least Significant Bits (LSBs) of a 16-bit word, you AND it with `1111111100000000_2` (which is `FF00_16`).

---
