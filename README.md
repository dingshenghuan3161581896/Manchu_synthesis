

---

# Manchu_synthesis
A Manchu TTS model using transfer learning from Spanish and Mandarin Chinese.

## Resources
- Download the CSS10 Spanish and Mandarin Chinese speech datasets used for training from: [CSS10 GitHub](https://github.com/Kyubyong/css10)
- The Manchu speech data and corresponding lab files are divided into three compressed files, named "manchu1", "manchu2" and "manchu3".
- Download the Montreal Forced Aligner from: [Montreal Forced Aligner GitHub](https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner)
- Download FastSpeech 2 from: [FastSpeech 2 GitHub](https://github.com/ming024/FastSpeech2)
- Download the Manchu pronunciation dictionary with 782 entries, along with the modified Spanish and Chinese pronunciation dictionaries from this GitHub page.

## Instructions
You can train the acoustic models for these three languages using the `mfa train` command. For detailed instructions, please refer to the [Montreal Forced Aligner GitHub](https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner).

### Steps:
1. Activate your environment. The language used is Python.
2. Modify the text/symbol.py: When train cn or cnm, please use these symbols:{'ɛ', 'tɕ', 'tʃ', 'pʰ', 'ʁ', 's', 'ɥ', 'w', 'kʰ', 'u', 'y', 'œ', 'ɾ', 'a', 'æ', 'ŋ', 'ʊ', 'e', 'k', 'i', 'o', 'ʊŋ', 'm', 'iŋ', 'tʰ', 'ɪ', 'ʂ', 'ɪŋ', 'ɻ', 'sil', 'aŋ', 'ɔ', 'ɢ', 'ʈʂ', 'ɕ', 'ʈʂʰ', 'tɕʰ', 'ɯ', 'tsʰ', 'ə', 'ʐ', 'p', 'v', 't', 'ɑ', 'z', 'x', 'f', 'ç', 'j', 'oŋ', 'ɣ', 'n', 'spn', 'l', 'ɚ', 'ɑŋ', 'ɤ', 'ɤŋ'}
When train es or esm, please use these symbols: {'kʰ', 'k', 'v', 'j', 'ɲ', 'ɡ', 'tɕʰ', 'ɾ', 's', 'θ', 'ɤŋ', 'β', 'y', 't̪', 'tʰ', 'aŋ', 'ʈʂʰ', 'ʃ', 'ɔ', 'd̪', 'ɢ', 'ŋ', 'ʝ', 'ʐ', 'm', 'x', 'sil', 'ç', 'ʂ', 'oŋ', 'e', 'tʃ', 'z', 'ɟ', 'spn', 'l', 'iŋ', 'ʁ', 'b', 'ɤ', 'p', 'æ', 'w', 'i', 'u', 'ʌ', 'c', 't͡s', 'a', 'ɯ', 'tɕ', 'ɟʝ', 'pʰ', 'ʎ', 't', 'f', 'ɣ', 'r', 'n', 'o', 'ð'}
3. Validate the Spanish and Mandarin Chinese audio files. Use the following command as a reference:
    ```bash
    mfa validate /path/to/your/audio_and_lab_files/ /path/to/your/dictionary/ --single_speaker -j 8 -t /path/to/validate_output/ --clean
    ```
4. Train the acoustic model. Use the following command as a reference:
    ```bash
    mfa train /path/to/your/audio_and_lab_files/ /path/to/your/dictionary/ /path/to/output/acoustic_model/acoustic_model.zip
    ```
5. Align the Spanish and Mandarin Chinese audio files. Use the following command as a reference:
    ```bash
    mfa align /path/to/your/audio_and_lab_files/ /path/to/your/dictionary/ /path/to/your/acoustic_model/ /path/to/output/TextGrid/ --single_speaker -j 8 -t /path/to/validate_output/ --no_textgrid_cleanup
    ```
6. Preprocess the data. Use the following command as a reference:
    ```bash
    python3 preprocess.py config/your_language/preprocess.yaml
    ```
    Please configure the corresponding language in the `config` folder to execute this step. The config files used in our experiments are available as a compressed package on this GitHub page.
7. Train the model. Use the following command as a reference:
    ```bash
    python3 train.py -p config/your_language/preprocess.yaml -m config/your_language/model.yaml -t config/your_language/train.yaml --restore_step 100000
    ```
8. Validate the Manchu audio files as described in step 2.
9. Train the Manchu acoustic model as described in step 3.
10. Align the Manchu audio files as described in step 4.
11. Preprocess the Manchu audio files as described in step 5.
12. Fine-tune the Manchu audio files. For example, using Spanish transfer learning to Manchu (esm), starting from the 100k checkpoint, use the following command:
    ```bash
    python3 train.py -p config/esm/preprocess.yaml -m config/esm/model.yaml -t config/esm/train.yaml --restore_step 100000
    ```
13. Synthesize audio. Use the following command as a reference:
    ```bash
    python3 synthesize.py --text "baturu, ere hergen be adarame hvlambi" --restore_step 200000 --mode single -p config/cnm/preprocess.yaml -m config/cnm/model.yaml -t config/cnm/train.yaml
    ```

Please follow the above steps to reproduce our experiments and train your own models. For more details and configuration files, refer to the provided links and resources.

---

Feel free to customize this further as per your needs.
