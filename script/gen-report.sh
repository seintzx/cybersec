#!/usr/bin/env bash

BASEDIR="`pwd`"
# BASEDIR="${HOME}/documents/csdc/monthly"
OUTPUTDIR="${BASEDIR}/report"
STYLEDIR="${BASEDIR}/style"
# DATENAME="`date +%Y-%B`"
DATENAME="`date +%Y-%m`"
REPORTNAME="monthly-report-${DATENAME}"
REPORTDIR="${OUTPUTDIR}/${DATENAME}"
LANGUAGE=it

CUSTOMER=(aea astra brunello cuticonsai day deda ducati fercam graniti hupac loccioni md mta novanext omp poltrona refresco sacbo sole stroili terzani)

make-pdf () {
    pandoc "${REPORTDIR}/${REPORTNAME}.md" \
        -o "${REPORTDIR}/${REPORTNAME}.pdf" \
        -H "${STYLEDIR}/preamble.tex" \
        --template="${STYLEDIR}/template.tex" \
        --highlight-style pygments \
        -V fontsize=12pt \
        -V lang=${LANGUAGE} \
        -V mainlang=${LANGUAGE} \
        -V papersize=a4paper \
        -V documentclass=report \
        -V tables \
        -N \
        --pdf-engine=xelatex
}

make-file () {
    FN="${REPORTDIR}/${REPORTNAME}.md"
    touch "${FN}"
    for f in ${CUSTOMER[@]}
    do
        echo "# $(echo ${f} | tr '[:lower:]' '[:upper:]')" >> "${FN}"
        echo "" >> "${FN}"
        echo "## Incidenti Rilevanti" >> "${FN}"
        echo "" >> "${FN}"
        echo "## Attvità in corso" >> "${FN}"
        echo "" >> "${FN}"
        echo "" >> "${FN}"
    done
}

if [ ! -d ${REPORTDIR} ] ; then mkdir -p ${REPORTDIR} ; fi
if [ -e "${REPORTDIR}/${REPORTNAME}.md" ]
then
    make-pdf
else
    make-file
fi
