    function convert() {
      //
      //  Get the TeX input
      //
      var input = document.getElementById("input").value.trim();
      //
      //  Clear the old output
      //
      output = document.getElementById('output');
      output.innerHTML = '';
      //
      //  Reset the tex labels (and automatic equation numbers, though there aren't any here).
      //  Get the conversion options (metrics and display settings)
      //  Convert the input to CommonHTML output and use a promise to wait for it to be ready
      //    (in case an extension needs to be loaded dynamically).
      //
      MathJax.texReset();
      var options = MathJax.getMetricsFor(output);
      MathJax.tex2chtmlPromise(input, options).then(function (node) {
        //
        //  The promise returns the typeset node, which we add to the output
        //  Then update the document to include the adjusted CSS for the
        //    content of the new equation.
        //
        output.appendChild(node);
        MathJax.startup.document.clear();
        MathJax.startup.document.updateDocument();
      }).catch(function (err) {
        //
        //  If there was an error, put the message into the output instead
        //
        output.appendChild(document.createElement('pre')).appendChild(document.createTextNode(err.message));
      }).then(function () {
        //
        //  Error or not, re-enable the display and render buttons
        //
      });
    }

    function changeText() {
      var input = document.getElementById("textp").value.trim();
      MathJax.texReset();
      var options = MathJax.getMetricsFor();
    }