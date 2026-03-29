+++
date = '2026-03-29T16:54:05+05:30'
title = 'COA'
+++

> ###### written by: Gemini

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
