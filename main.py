
import streamlit as st # pip install streamlit==0.82.0
import os
import datetime
import pandas as pd
import numpy as np
import dl_translate as dlt



st.set_page_config(page_title='Translation tool', page_icon='translator-icon.png', layout='wide', initial_sidebar_state='expanded')

def main():
    menu = ["Translation page","Click here to contribute some text to help improve the translation tool"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Translation page":
        Languages = {'afrikaans':'af','albanian':'sq','amharic':'am','arabic':'ar','armenian':'hy','azerbaijani':'az','basque':'eu','belarusian':'be','bengali':'bn','bosnian':'bs','bulgarian':'bg','catalan':'ca','cebuano':'ceb','chichewa':'ny','chinese (simplified)':'zh-cn','chinese (traditional)':'zh-tw','corsican':'co','croatian':'hr','czech':'cs','danish':'da','dutch':'nl','english':'en','esperanto':'eo','estonian':'et','filipino':'tl','finnish':'fi','french':'fr','frisian':'fy','galician':'gl','georgian':'ka','german':'de','greek':'el','gujarati':'gu','haitian creole':'ht','hausa':'ha','hawaiian':'haw','hebrew':'iw','hebrew':'he','hindi':'hi','hmong':'hmn','hungarian':'hu','icelandic':'is','igbo':'ig','indonesian':'id','irish':'ga','italian':'it','japanese':'ja','javanese':'jw','kannada':'kn','kazakh':'kk','khmer':'km','korean':'ko','kurdish (kurmanji)':'ku','kyrgyz':'ky','lao':'lo','latin':'la','latvian':'lv','lithuanian':'lt','luxembourgish':'lb','macedonian':'mk','malagasy':'mg','malay':'ms','malayalam':'ml','maltese':'mt','maori':'mi','marathi':'mr','mongolian':'mn','myanmar (burmese)':'my','nepali':'ne','norwegian':'no','odia':'or','pashto':'ps','persian':'fa','polish':'pl','portuguese':'pt','punjabi':'pa','romanian':'ro','russian':'ru','samoan':'sm','scots gaelic':'gd','serbian':'sr','sesotho':'st','shona':'sn','sindhi':'sd','sinhala':'si','slovak':'sk','slovenian':'sl','somali':'so','spanish':'es','sundanese':'su','swahili':'sw','swedish':'sv','tajik':'tg','tamil':'ta','telugu':'te','thai':'th','turkish':'tr','turkmen':'tk','ukrainian':'uk','urdu':'ur','uyghur':'ug','uzbek':'uz','vietnamese':'vi','welsh':'cy','xhosa':'xh','yiddish':'yi','yoruba':'yo','zulu':'zu'}



        st.title("Language Translator:balloon:")
        st.write('''
        [![Star](https://img.shields.io/github/stars/HarisankarSNair/LanguageTranslator.svg?logo=github&style=social)](https://gitHub.com/HarisankarSNair/LanguageTranslator)
        &nbsp [![Streamlit](https://img.shields.io/badge/Made%20with%20-Streamlit-red)](https://streamlit.io/)
        ''')

        text = st.text_area("Enter text:",height=None,max_chars=None,key=None,help="Enter your text here")

        option1 = st.selectbox('Input language',('english', 'afrikaans', 'albanian', 'amharic', 'arabic', 'armenian', 'azerbaijani', 'basque', 'belarusian', 'bengali', 'bosnian', 'bulgarian', 'catalan', 'cebuano', 'chichewa', 'chinese (simplified)', 'chinese (traditional)', 'corsican', 'croatian', 'czech', 'danish', 'dutch',  'esperanto', 'estonian', 'filipino', 'finnish', 'french', 'frisian', 'galician', 'georgian', 'german', 'greek', 'gujarati', 'haitian creole', 'hausa', 'hawaiian', 'hebrew', 'hindi', 'hmong', 'hungarian', 'icelandic', 'igbo', 'indonesian', 'irish', 'italian', 'japanese', 'javanese', 'kannada', 'kazakh', 'khmer', 'korean', 'kurdish (kurmanji)', 'kyrgyz', 'lao', 'latin', 'latvian', 'lithuanian', 'luxembourgish', 'macedonian', 'malagasy', 'malay', 'malayalam', 'maltese', 'maori', 'marathi', 'mongolian', 'myanmar (burmese)', 'nepali', 'norwegian', 'odia', 'pashto', 'persian', 'polish', 'portuguese', 'punjabi', 'romanian', 'russian', 'samoan', 'scots gaelic', 'serbian', 'sesotho', 'shona', 'sindhi', 'sinhala', 'slovak', 'slovenian', 'somali', 'spanish', 'sundanese', 'swahili', 'swedish', 'tajik', 'tamil', 'telugu', 'thai', 'turkish', 'turkmen', 'ukrainian', 'urdu', 'uyghur', 'uzbek', 'vietnamese', 'welsh', 'xhosa', 'yiddish', 'yoruba', 'zulu'))

        option2 = st.selectbox('Output language',('malayalam', 'afrikaans', 'albanian', 'amharic', 'arabic', 'armenian', 'azerbaijani', 'basque', 'belarusian', 'bengali', 'bosnian', 'bulgarian', 'catalan', 'cebuano', 'chichewa', 'chinese (simplified)', 'chinese (traditional)', 'corsican', 'croatian', 'czech', 'danish', 'dutch', 'english', 'esperanto', 'estonian', 'filipino', 'finnish', 'french', 'frisian', 'galician', 'georgian', 'german', 'greek', 'gujarati', 'haitian creole', 'hausa', 'hawaiian', 'hebrew', 'hindi', 'hmong', 'hungarian', 'icelandic', 'igbo', 'indonesian', 'irish', 'italian', 'japanese', 'javanese', 'kannada', 'kazakh', 'khmer', 'korean', 'kurdish (kurmanji)', 'kyrgyz', 'lao', 'latin', 'latvian', 'lithuanian', 'luxembourgish', 'macedonian', 'malagasy', 'malay', 'maltese', 'maori', 'marathi', 'mongolian', 'myanmar (burmese)', 'nepali', 'norwegian', 'odia', 'pashto', 'persian', 'polish', 'portuguese', 'punjabi', 'romanian', 'russian', 'samoan', 'scots gaelic', 'serbian', 'sesotho', 'shona', 'sindhi', 'sinhala', 'slovak', 'slovenian', 'somali', 'spanish', 'sundanese', 'swahili', 'swedish', 'tajik', 'tamil', 'telugu', 'thai', 'turkish', 'turkmen', 'ukrainian', 'urdu', 'uyghur', 'uzbek', 'vietnamese', 'welsh', 'xhosa', 'yiddish', 'yoruba', 'zulu'))

        value1 = Languages[option1]
        value2 = Languages[option2]
        mt = dlt.TranslationModel()
        if st.button('Translate Sentence'):
            if text == "":
                st.warning('Please **enter text** for translation')

            else:
                translate = mt.translate(text,source=value1,target=value2)
                st.info(str(translate))
                st.success("Translation is **successfully** completed!")
                st.balloons()
        else:
            pass


    if choice == "Click here to contribute some text to help improve the translation tool":
        csv_file = 'results.csv'
        if os.path.exists(csv_file):
            # read from file
            results_option1 = pd.read_csv(csv_file, index_col=False)
        else:
            # create empty dataframe with the right columns & dtypes
            results_option1 = pd.DataFrame(
                {'non english text': pd.Series(dtype='str'),
                'language': pd.Series(dtype='str'),
                'english text': pd.Series(dtype='str'),
                }
            )


        with st.form('input_form'):
            neavalue = st.text_input('Enter non english text:')
            lavalue = st.text_input('Which language are you using?')
            evalue = st.text_input('Translate it in english:')
            clickSubmit = st.form_submit_button('Submit')

        if clickSubmit:
            timestamp = datetime.datetime.now()
            results_option1.loc[len(results_option1)] = [neavalue, lavalue, evalue]
            results_option1.to_csv(csv_file, index=False)
            st.dataframe(results_option1)
        else:
            st.markdown("Please submit to save")

if __name__ == '__main__':
    main()