.. sectnum::
    :start: 1

Cabling SVG
----------------

    .. image:: ../../../_static/cabling/output/cabling.svg
        :target: ../../../_static/cabling/output/cabling.svg
        :width: 50%
        :align: center

3D model view in Raw HTML
--------------------------

    .. raw:: html

        <model-viewer src="path/to/3d_model.gltf" style="width: 30%; height: 100px; resize:both; overflow:auto;" alt="Description of the 3D model" camera-controls camera-orbit="90deg 0deg .01m" ></model-viewer>
       
PDF
----------

    .. pdf-include:: _static/hardware/EL-25-38-00-2_schematic.pdf#view=Fit

Drawio Rendering
--------------------

   .. drawio-image:: ../../../_static/software/diagrams/cmake_tree.drawio
      :format: svg
      :page-index: 0

Raw HTML
---------

   .. raw:: html

      <iframe src="path/index.html" height="2500px" width="100%"></iframe>

Image import
-------------

.. image:: _static/gui.png
    :scale: 100 %
    :alt: This is alternate text

Markdown import
----------------

.. mdinclude:: path/to/README.md

Code sections
--------------

.. code-block:: bash

   git clone https://github.com/ThrowTheSwitch/Unity.git

.. code-block:: bash

   pip3 install eel docopt

.. code-block:: text

    myproject/
    ├── conf.py
    ├── plantuml.jar
    ├── index.rst
    ├── _build/
    ├── _static/
    ├── _templates/
    └── modules/
        ├── module1.rst
        └── module2.rst

PlantUML rendering
---------------------

.. uml::

   Alice -> Bob: Hi!
   Alice <- Bob: How are you?     