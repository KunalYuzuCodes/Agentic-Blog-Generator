<!DOCTYPE html><html lang="en" class="js-focus-visible js" data-js-focus-visible=""><head>
    
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width,initial-scale=1">
      
        <meta name="description" content="Agent Framework / shim to use Pydantic with LLMs">
      
      
      
        <link rel="canonical" href="https://ai.pydantic.dev/api/pydantic_graph/mermaid/">
      
      
        <link rel="prev" href="../persistence/">
      
      
        <link rel="next" href="../exceptions/">
      
      
      <link rel="icon" href="../../../favicon.ico">
      <meta name="generator" content="mkdocs-1.6.1, mkdocs-material-9.6.5">
    
    
      
        <title>pydantic_graph.mermaid - PydanticAI</title>
      
    
    
      <link rel="stylesheet" href="../../../assets/stylesheets/main.8608ea7d.min.css">
      
        
        <link rel="stylesheet" href="../../../assets/stylesheets/palette.06af60db.min.css">
      
      


    
    
      
    
    
      
        
        
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,300i,400,400i,700,700i%7CRoboto+Mono:400,400i,700,700i&amp;display=fallback">
        <style>:root{--md-text-font:"Roboto";--md-code-font:"Roboto Mono"}</style>
      
    
    
      <link rel="stylesheet" href="../../../assets/_mkdocstrings.css">
    
      <link rel="stylesheet" href="../../../extra/tweaks.css">
    
    <script>__md_scope=new URL("../../..",location),__md_hash=e=>[...e].reduce(((e,_)=>(e<<5)-e+_.charCodeAt(0)),0),__md_get=(e,_=localStorage,t=__md_scope)=>JSON.parse(_.getItem(t.pathname+"."+e)),__md_set=(e,_,t=localStorage,a=__md_scope)=>{try{t.setItem(a.pathname+"."+e,JSON.stringify(_))}catch(e){}}</script>
    
      

    
    
      
        <meta property="og:type" content="website">
      
        <meta property="og:title" content="pydantic_graph.mermaid - PydanticAI">
      
        <meta property="og:description" content="Agent Framework / shim to use Pydantic with LLMs">
      
        <meta property="og:image" content="https://ai.pydantic.dev/assets/images/social/api/pydantic_graph/mermaid.png">
      
        <meta property="og:image:type" content="image/png">
      
        <meta property="og:image:width" content="1200">
      
        <meta property="og:image:height" content="630">
      
        <meta property="og:url" content="https://ai.pydantic.dev/api/pydantic_graph/mermaid/">
      
        <meta name="twitter:card" content="summary_large_image">
      
        <meta name="twitter:title" content="pydantic_graph.mermaid - PydanticAI">
      
        <meta name="twitter:description" content="Agent Framework / shim to use Pydantic with LLMs">
      
        <meta name="twitter:image" content="https://ai.pydantic.dev/assets/images/social/api/pydantic_graph/mermaid.png">
      
    
    
   <link href="../../../assets/stylesheets/glightbox.min.css" rel="stylesheet"><style>
    html.glightbox-open { overflow: initial; height: 100%; }
    .gslide-title { margin-top: 0px; user-select: text; }
    .gslide-desc { color: #666; user-select: text; }
    .gslide-image img { background: white; }
    .gscrollbar-fixer { padding-right: 15px; }
    .gdesc-inner { font-size: 0.75rem; }
    body[data-md-color-scheme="slate"] .gdesc-inner { background: var(--md-default-bg-color);}
    body[data-md-color-scheme="slate"] .gslide-title { color: var(--md-default-fg-color);}
    body[data-md-color-scheme="slate"] .gslide-desc { color: var(--md-default-fg-color);}</style> <script src="../../../assets/javascripts/glightbox.min.js"></script><meta name="theme-color" content="#e92063"><meta name="color-scheme" content="light"></head>
  
  
    
    
      
    
    
    
    
    <body dir="ltr" data-md-color-scheme="default" data-md-color-primary="pink" data-md-color-accent="pink" data-md-color-media="(prefers-color-scheme)">
  
    
    <input class="md-toggle" data-md-toggle="drawer" type="checkbox" id="__drawer" autocomplete="off">
    <input class="md-toggle" data-md-toggle="search" type="checkbox" id="__search" autocomplete="off">
    <label class="md-overlay" for="__drawer"></label>
    <div data-md-component="skip">
      
        
        <a href="#pydantic_graphmermaid" class="md-skip">
          Skip to content
        </a>
      
    </div>
    <div data-md-component="announce">
      
    </div>
    
    
      

  

<header class="md-header md-header--shadow" data-md-component="header">
  <nav class="md-header__inner md-grid" aria-label="Header">
    <a href="../../.." title="PydanticAI" class="md-header__button md-logo" aria-label="PydanticAI" data-md-component="logo">
      
  <img src="../../../img/logo-white.svg" alt="logo">

    </a>
    <label class="md-header__button md-icon" for="__drawer">
      
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M3 6h18v2H3zm0 5h18v2H3zm0 5h18v2H3z"></path></svg>
    </label>
    <div class="md-header__title" data-md-component="header-title">
      <div class="md-header__ellipsis">
        <div class="md-header__topic">
          <span class="md-ellipsis">
            PydanticAI
          </span>
        </div>
        <div class="md-header__topic" data-md-component="header-topic">
          <span class="md-ellipsis">
            
              pydantic_graph.mermaid
            
          </span>
        </div>
      </div>
    </div>
    
      
        <form class="md-header__option" data-md-component="palette">
  
    
    
    
    <input class="md-option" data-md-color-media="(prefers-color-scheme)" data-md-color-scheme="default" data-md-color-primary="pink" data-md-color-accent="pink" aria-label="Switch to light mode" type="radio" name="__palette" id="__palette_0">
    
      <label class="md-header__button md-icon" title="Switch to light mode" for="__palette_1">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 2a7 7 0 0 0-7 7c0 2.38 1.19 4.47 3 5.74V17a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1v-2.26c1.81-1.27 3-3.36 3-5.74a7 7 0 0 0-7-7M9 21a1 1 0 0 0 1 1h4a1 1 0 0 0 1-1v-1H9z"></path></svg>
      </label>
    
  
    
    
    
    <input class="md-option" data-md-color-media="(prefers-color-scheme: light)" data-md-color-scheme="default" data-md-color-primary="pink" data-md-color-accent="pink" aria-label="Switch to dark mode" type="radio" name="__palette" id="__palette_1">
    
      <label class="md-header__button md-icon" title="Switch to dark mode" for="__palette_2" hidden="">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 2a7 7 0 0 1 7 7c0 2.38-1.19 4.47-3 5.74V17a1 1 0 0 1-1 1H9a1 1 0 0 1-1-1v-2.26C6.19 13.47 5 11.38 5 9a7 7 0 0 1 7-7M9 21v-1h6v1a1 1 0 0 1-1 1h-4a1 1 0 0 1-1-1m3-17a5 5 0 0 0-5 5c0 2.05 1.23 3.81 3 4.58V16h4v-2.42c1.77-.77 3-2.53 3-4.58a5 5 0 0 0-5-5"></path></svg>
      </label>
    
  
    
    
    
    <input class="md-option" data-md-color-media="(prefers-color-scheme: dark)" data-md-color-scheme="slate" data-md-color-primary="pink" data-md-color-accent="pink" aria-label="Switch to system preference" type="radio" name="__palette" id="__palette_2">
    
      <label class="md-header__button md-icon" title="Switch to system preference" for="__palette_0" hidden="">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M9 2c3.87 0 7 3.13 7 7 0 2.38-1.19 4.47-3 5.74V17c0 .55-.45 1-1 1H6c-.55 0-1-.45-1-1v-2.26C3.19 13.47 2 11.38 2 9c0-3.87 3.13-7 7-7M6 21v-1h6v1c0 .55-.45 1-1 1H7c-.55 0-1-.45-1-1M9 4C6.24 4 4 6.24 4 9c0 2.05 1.23 3.81 3 4.58V16h4v-2.42c1.77-.77 3-2.53 3-4.58 0-2.76-2.24-5-5-5m10 9h-2l-3.2 9h1.9l.7-2h3.2l.7 2h1.9zm-2.15 5.65L18 15l1.15 3.65z"></path></svg>
      </label>
    
  
</form>
      
    
    
      <script>var palette=__md_get("__palette");if(palette&&palette.color){if("(prefers-color-scheme)"===palette.color.media){var media=matchMedia("(prefers-color-scheme: light)"),input=document.querySelector(media.matches?"[data-md-color-media='(prefers-color-scheme: light)']":"[data-md-color-media='(prefers-color-scheme: dark)']");palette.color.media=input.getAttribute("data-md-color-media"),palette.color.scheme=input.getAttribute("data-md-color-scheme"),palette.color.primary=input.getAttribute("data-md-color-primary"),palette.color.accent=input.getAttribute("data-md-color-accent")}for(var[key,value]of Object.entries(palette.color))document.body.setAttribute("data-md-color-"+key,value)}</script>
    
    
    
      <label class="md-header__button md-icon" for="__search">
        
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M9.5 3A6.5 6.5 0 0 1 16 9.5c0 1.61-.59 3.09-1.56 4.23l.27.27h.79l5 5-1.5 1.5-5-5v-.79l-.27-.27A6.52 6.52 0 0 1 9.5 16 6.5 6.5 0 0 1 3 9.5 6.5 6.5 0 0 1 9.5 3m0 2C7 5 5 7 5 9.5S7 14 9.5 14 14 12 14 9.5 12 5 9.5 5"></path></svg>
      </label>
      <div class="md-search" role="dialog">
  <label class="md-search__overlay" for="__search"></label>
  <div class="md-search__inner" role="search">
    <form class="md-search__form" name="search">
      <input type="text" id="searchbox" class="md-search__input" name="query" aria-label="Search" placeholder="Search" autocapitalize="off" autocorrect="off" autocomplete="off" spellcheck="false" required="">
      <label class="md-search__icon md-icon" for="__search">

        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M9.5 3A6.5 6.5 0 0 1 16 9.5c0 1.61-.59 3.09-1.56 4.23l.27.27h.79l5 5-1.5 1.5-5-5v-.79l-.27-.27A6.516 6.516 0 0 1 9.5 16 6.5 6.5 0 0 1 3 9.5 6.5 6.5 0 0 1 9.5 3m0 2C7 5 5 7 5 9.5S7 14 9.5 14 14 12 14 9.5 12 5 9.5 5Z"></path></svg>

        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M20 11v2H8l5.5 5.5-1.42 1.42L4.16 12l7.92-7.92L13.5 5.5 8 11h12Z"></path></svg>
      </label>
      <nav class="md-search__options" aria-label="Search">

        <button id="searchbox-clear" type="reset" class="md-search__icon md-icon" title="Clear" aria-label="Clear" tabindex="-1">

          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M19 6.41 17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12 19 6.41Z"></path></svg>
        </button>
      </nav>

        <div class="md-search__suggest"></div>

    </form>
    <div class="md-search__output">
      <div class="md-search__scrollwrap" tabindex="0">
        <div class="md-search-result">
          <div class="md-search-result__meta" id="type-to-start-searching">Type to start searching</div>
          <ol class="md-search-result__list" id="hits" role="presentation" hidden=""></ol>
        </div>
      </div>
    </div>
  </div>
</div>
    
    
      <div class="md-header__source">
        <a href="https://github.com/pydantic/pydantic-ai" title="Go to repository" class="md-source" data-md-component="source">
  <div class="md-source__icon md-icon">
    
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><!--! Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) Copyright 2024 Fonticons, Inc.--><path d="M439.55 236.05 244 40.45a28.87 28.87 0 0 0-40.81 0l-40.66 40.63 51.52 51.52c27.06-9.14 52.68 16.77 43.39 43.68l49.66 49.66c34.23-11.8 61.18 31 35.47 56.69-26.49 26.49-70.21-2.87-56-37.34L240.22 199v121.85c25.3 12.54 22.26 41.85 9.08 55a34.34 34.34 0 0 1-48.55 0c-17.57-17.6-11.07-46.91 11.25-56v-123c-20.8-8.51-24.6-30.74-18.64-45L142.57 101 8.45 235.14a28.86 28.86 0 0 0 0 40.81l195.61 195.6a28.86 28.86 0 0 0 40.8 0l194.69-194.69a28.86 28.86 0 0 0 0-40.81"></path></svg>
  </div>
  <div class="md-source__repository md-source__repository--active">
    pydantic/pydantic-ai
  <ul class="md-source__facts"><li class="md-source__fact md-source__fact--version">v0.0.50</li><li class="md-source__fact md-source__fact--stars">8k</li><li class="md-source__fact md-source__fact--forks">687</li></ul></div>
</a>
      </div>
    
  </nav>
  
</header>
    
    <div class="md-container" data-md-component="container">
      
      
        
          
        
      
      <main class="md-main" data-md-component="main">
        <div class="md-main__inner md-grid">
          
            
              
              <div class="md-sidebar md-sidebar--primary" data-md-component="sidebar" data-md-type="navigation">
                <div class="md-sidebar__scrollwrap">
                  <div class="md-sidebar__inner">
                    



<nav class="md-nav md-nav--primary" aria-label="Navigation" data-md-level="0">
  <label class="md-nav__title" for="__drawer">
    <a href="../../.." title="PydanticAI" class="md-nav__button md-logo" aria-label="PydanticAI" data-md-component="logo">
      
  <img src="../../../img/logo-white.svg" alt="logo">

    </a>
    PydanticAI
  </label>
  
    <div class="md-nav__source">
      <a href="https://github.com/pydantic/pydantic-ai" title="Go to repository" class="md-source" data-md-component="source">
  <div class="md-source__icon md-icon">
    
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><!--! Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) Copyright 2024 Fonticons, Inc.--><path d="M439.55 236.05 244 40.45a28.87 28.87 0 0 0-40.81 0l-40.66 40.63 51.52 51.52c27.06-9.14 52.68 16.77 43.39 43.68l49.66 49.66c34.23-11.8 61.18 31 35.47 56.69-26.49 26.49-70.21-2.87-56-37.34L240.22 199v121.85c25.3 12.54 22.26 41.85 9.08 55a34.34 34.34 0 0 1-48.55 0c-17.57-17.6-11.07-46.91 11.25-56v-123c-20.8-8.51-24.6-30.74-18.64-45L142.57 101 8.45 235.14a28.86 28.86 0 0 0 0 40.81l195.61 195.6a28.86 28.86 0 0 0 40.8 0l194.69-194.69a28.86 28.86 0 0 0 0-40.81"></path></svg>
  </div>
  <div class="md-source__repository md-source__repository--active">
    pydantic/pydantic-ai
  <ul class="md-source__facts"><li class="md-source__fact md-source__fact--version">v0.0.50</li><li class="md-source__fact md-source__fact--stars">8k</li><li class="md-source__fact md-source__fact--forks">687</li></ul></div>
</a>
    </div>
  
  <ul class="md-nav__list">
    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../../.." class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Introduction
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../install/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Installation
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../help/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Getting Help
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../contributing/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Contributing
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../troubleshooting/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Troubleshooting
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    
    
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
    
    
      
        
        
      
    
    
    <li class="md-nav__item md-nav__item--section md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_6">
        
          
          <label class="md-nav__link" for="__nav_6" id="__nav_6_label" tabindex="">
            
  
  <span class="md-ellipsis">
    Documentation
    
  </span>
  

            <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_6_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_6">
            <span class="md-nav__icon md-icon"></span>
            Documentation
          </label>
          <ul class="md-nav__list">
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../agents/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Agents
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../models/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Models
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../dependencies/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Dependencies
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Function Tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../common-tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Common Tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../results/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Results
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../message-history/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Messages and chat history
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../testing/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Unit testing
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../logfire/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Debugging and Monitoring
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../multi-agent-applications/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Multi-agent Applications
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../graph/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Graphs
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../evals/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Evals
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../input/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Image, Audio &amp; Document Input
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    
    
      
        
          
        
      
        
      
        
      
        
      
    
    
      
    
    
    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_6_14">
        
          
          
          <div class="md-nav__link md-nav__container">
            <a href="../../../mcp/" class="md-nav__link ">
              
  
  <span class="md-ellipsis">
    MCP
    
  </span>
  

            </a>
            
              
              <label class="md-nav__link " for="__nav_6_14" id="__nav_6_14_label" tabindex="0">
                <span class="md-nav__icon md-icon"></span>
              </label>
            
          </div>
        
        <nav class="md-nav" data-md-level="2" aria-labelledby="__nav_6_14_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_6_14">
            <span class="md-nav__icon md-icon"></span>
            MCP
          </label>
          <ul class="md-nav__list">
            
              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../mcp/client/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Client
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../mcp/server/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Server
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../mcp/run-python/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    MCP Run Python
    
  </span>
  

      </a>
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../cli/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Command Line Interface (CLI)
    
  </span>
  

      </a>
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

    
      
      
  
  
  
  
    
    
      
        
          
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
    
    
      
        
        
      
    
    
    <li class="md-nav__item md-nav__item--section md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_7">
        
          
          
          <div class="md-nav__link md-nav__container">
            <a href="../../../examples/" class="md-nav__link ">
              
  
  <span class="md-ellipsis">
    Examples
    
  </span>
  

            </a>
            
              
              <label class="md-nav__link " for="__nav_7" id="__nav_7_label" tabindex="">
                <span class="md-nav__icon md-icon"></span>
              </label>
            
          </div>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_7_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_7">
            <span class="md-nav__icon md-icon"></span>
            Examples
          </label>
          <ul class="md-nav__list">
            
              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../examples/pydantic-model/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Pydantic Model
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../examples/weather-agent/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Weather agent
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../examples/bank-support/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Bank support
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../examples/sql-gen/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    SQL Generation
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../examples/flight-booking/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Flight booking
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../examples/rag/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    RAG
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../examples/stream-markdown/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Stream markdown
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../examples/stream-whales/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Stream whales
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../examples/chat-app/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Chat App with FastAPI
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../examples/question-graph/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Question Graph
    
  </span>
  

      </a>
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

    
      
      
  
  
    
  
  
  
    
    
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
    
    
      
        
        
      
    
    
    <li class="md-nav__item md-nav__item--active md-nav__item--section md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_8" checked="">
        
          
          <label class="md-nav__link" for="__nav_8" id="__nav_8_label" tabindex="">
            
  
  <span class="md-ellipsis">
    API Reference
    
  </span>
  

            <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_8_label" aria-expanded="true">
          <label class="md-nav__title" for="__nav_8">
            <span class="md-nav__icon md-icon"></span>
            API Reference
          </label>
          <ul class="md-nav__list">
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../agent/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.agent
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../common_tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.common_tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../result/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.result
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../messages/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.messages
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../exceptions/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.exceptions
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../settings/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.settings
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../usage/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.usage
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../mcp/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.mcp
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../format_as_xml/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.format_as_xml
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/base/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/openai/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.openai
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/anthropic/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.anthropic
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/bedrock/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.bedrock
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/cohere/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.cohere
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/gemini/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.gemini
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/groq/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.groq
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/instrumented/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.instrumented
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/mistral/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.mistral
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/test/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.test
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/function/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.function
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/fallback/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.fallback
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/wrapper/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.wrapper
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../providers/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.providers
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../graph/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../nodes/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.nodes
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../persistence/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.persistence
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
    
  
  
  
    <li class="md-nav__item md-nav__item--active">
      
      <input class="md-nav__toggle md-toggle" type="checkbox" id="__toc">
      
      
        
      
      
        <label class="md-nav__link md-nav__link--active" for="__toc">
          
  
  <span class="md-ellipsis">
    pydantic_graph.mermaid
    
  </span>
  

          <span class="md-nav__icon md-icon"></span>
        </label>
      
      <a href="./" class="md-nav__link md-nav__link--active">
        
  
  <span class="md-ellipsis">
    pydantic_graph.mermaid
    
  </span>
  

      </a>
      
        

<nav class="md-nav md-nav--secondary" aria-label="Table of contents">
  
  
  
    
  
  
    <label class="md-nav__title" for="__toc">
      <span class="md-nav__icon md-icon"></span>
      Table of contents
    </label>
    <ul class="md-nav__list" data-md-component="toc">
      
        <li class="md-nav__item">
  <a href="#pydantic_graph.mermaid" class="md-nav__link">
    <span class="md-ellipsis">
      mermaid
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_graph.mermaid.DEFAULT_HIGHLIGHT_CSS" class="md-nav__link">
    <span class="md-ellipsis">
      DEFAULT_HIGHLIGHT_CSS
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_graph.mermaid.StateDiagramDirection" class="md-nav__link">
    <span class="md-ellipsis">
      StateDiagramDirection
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_graph.mermaid.generate_code" class="md-nav__link">
    <span class="md-ellipsis">
      generate_code
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_graph.mermaid.request_image" class="md-nav__link">
    <span class="md-ellipsis">
      request_image
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_graph.mermaid.save_image" class="md-nav__link">
    <span class="md-ellipsis">
      save_image
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_graph.mermaid.MermaidConfig" class="md-nav__link">
    <span class="md-ellipsis">
      MermaidConfig
    </span>
  </a>
  
    <nav class="md-nav" aria-label="MermaidConfig">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.mermaid.MermaidConfig.start_node" class="md-nav__link">
    <span class="md-ellipsis">
      start_node
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.mermaid.MermaidConfig.highlighted_nodes" class="md-nav__link">
    <span class="md-ellipsis">
      highlighted_nodes
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.mermaid.MermaidConfig.highlight_css" class="md-nav__link">
    <span class="md-ellipsis">
      highlight_css
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.mermaid.MermaidConfig.title" class="md-nav__link">
    <span class="md-ellipsis">
      title
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.mermaid.MermaidConfig.edge_labels" class="md-nav__link">
    <span class="md-ellipsis">
      edge_labels
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.mermaid.MermaidConfig.notes" class="md-nav__link">
    <span class="md-ellipsis">
      notes
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.mermaid.MermaidConfig.image_type" class="md-nav__link">
    <span class="md-ellipsis">
      image_type
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.mermaid.MermaidConfig.pdf_fit" class="md-nav__link">
    <span class="md-ellipsis">
      pdf_fit
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.mermaid.MermaidConfig.pdf_landscape" class="md-nav__link">
    <span class="md-ellipsis">
      pdf_landscape
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.mermaid.MermaidConfig.pdf_paper" class="md-nav__link">
    <span class="md-ellipsis">
      pdf_paper
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.mermaid.MermaidConfig.background_color" class="md-nav__link">
    <span class="md-ellipsis">
      background_color
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.mermaid.MermaidConfig.theme" class="md-nav__link">
    <span class="md-ellipsis">
      theme
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.mermaid.MermaidConfig.width" class="md-nav__link">
    <span class="md-ellipsis">
      width
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.mermaid.MermaidConfig.height" class="md-nav__link">
    <span class="md-ellipsis">
      height
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.mermaid.MermaidConfig.scale" class="md-nav__link">
    <span class="md-ellipsis">
      scale
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.mermaid.MermaidConfig.httpx_client" class="md-nav__link">
    <span class="md-ellipsis">
      httpx_client
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.mermaid.MermaidConfig.direction" class="md-nav__link">
    <span class="md-ellipsis">
      direction
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_graph.mermaid.NodeIdent" class="md-nav__link">
    <span class="md-ellipsis">
      NodeIdent
    </span>
  </a>
  
</li>
      
    </ul>
  
</nav>
      
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../exceptions/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.exceptions
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../pydantic_evals/dataset/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.dataset
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../pydantic_evals/evaluators/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.evaluators
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../pydantic_evals/reporting/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.reporting
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../pydantic_evals/otel/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.otel
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../pydantic_evals/generation/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.generation
    
  </span>
  

      </a>
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

    
  </ul>
</nav>
                  </div>
                </div>
              </div>
            
            
              
              <div class="md-sidebar md-sidebar--secondary" data-md-component="sidebar" data-md-type="toc" style="top: 48px;">
                <div class="md-sidebar__scrollwrap" style="height: 474px;">
                  <div class="md-sidebar__inner">
                    

<nav class="md-nav md-nav--secondary" aria-label="Table of contents">
  
  
  
    
  
  
    <label class="md-nav__title" for="__toc">
      <span class="md-nav__icon md-icon"></span>
      Table of contents
    </label>
    <ul class="md-nav__list" data-md-component="toc">
      
        <li class="md-nav__item">
  <a href="#pydantic_graph.mermaid" class="md-nav__link">
    <span class="md-ellipsis">
      mermaid
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_graph.mermaid.DEFAULT_HIGHLIGHT_CSS" class="md-nav__link">
    <span class="md-ellipsis">
      DEFAULT_HIGHLIGHT_CSS
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_graph.mermaid.StateDiagramDirection" class="md-nav__link">
    <span class="md-ellipsis">
      StateDiagramDirection
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_graph.mermaid.generate_code" class="md-nav__link">
    <span class="md-ellipsis">
      generate_code
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_graph.mermaid.request_image" class="md-nav__link">
    <span class="md-ellipsis">
      request_image
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_graph.mermaid.save_image" class="md-nav__link">
    <span class="md-ellipsis">
      save_image
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_graph.mermaid.MermaidConfig" class="md-nav__link">
    <span class="md-ellipsis">
      MermaidConfig
    </span>
  </a>
  
    <nav class="md-nav" aria-label="MermaidConfig">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.mermaid.MermaidConfig.start_node" class="md-nav__link">
    <span class="md-ellipsis">
      start_node
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.mermaid.MermaidConfig.highlighted_nodes" class="md-nav__link">
    <span class="md-ellipsis">
      highlighted_nodes
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.mermaid.MermaidConfig.highlight_css" class="md-nav__link">
    <span class="md-ellipsis">
      highlight_css
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.mermaid.MermaidConfig.title" class="md-nav__link">
    <span class="md-ellipsis">
      title
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.mermaid.MermaidConfig.edge_labels" class="md-nav__link">
    <span class="md-ellipsis">
      edge_labels
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.mermaid.MermaidConfig.notes" class="md-nav__link">
    <span class="md-ellipsis">
      notes
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.mermaid.MermaidConfig.image_type" class="md-nav__link">
    <span class="md-ellipsis">
      image_type
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.mermaid.MermaidConfig.pdf_fit" class="md-nav__link">
    <span class="md-ellipsis">
      pdf_fit
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.mermaid.MermaidConfig.pdf_landscape" class="md-nav__link">
    <span class="md-ellipsis">
      pdf_landscape
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.mermaid.MermaidConfig.pdf_paper" class="md-nav__link">
    <span class="md-ellipsis">
      pdf_paper
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.mermaid.MermaidConfig.background_color" class="md-nav__link">
    <span class="md-ellipsis">
      background_color
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.mermaid.MermaidConfig.theme" class="md-nav__link">
    <span class="md-ellipsis">
      theme
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.mermaid.MermaidConfig.width" class="md-nav__link">
    <span class="md-ellipsis">
      width
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.mermaid.MermaidConfig.height" class="md-nav__link">
    <span class="md-ellipsis">
      height
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.mermaid.MermaidConfig.scale" class="md-nav__link">
    <span class="md-ellipsis">
      scale
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.mermaid.MermaidConfig.httpx_client" class="md-nav__link">
    <span class="md-ellipsis">
      httpx_client
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_graph.mermaid.MermaidConfig.direction" class="md-nav__link">
    <span class="md-ellipsis">
      direction
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_graph.mermaid.NodeIdent" class="md-nav__link">
    <span class="md-ellipsis">
      NodeIdent
    </span>
  </a>
  
</li>
      
    </ul>
  
</nav>
                  </div>
                </div>
              </div>
            
          
          
            <div class="md-content" data-md-component="content">
              <article class="md-content__inner md-typeset">
                
                  


  
  


<h1 id="pydantic_graphmermaid"><code>pydantic_graph.mermaid</code></h1>


<div class="doc doc-object doc-module">



<a id="pydantic_graph.mermaid"></a>
    <div class="doc doc-contents first">








  <div class="doc doc-children">















<div class="doc doc-object doc-attribute">



<h3 id="pydantic_graph.mermaid.DEFAULT_HIGHLIGHT_CSS" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">DEFAULT_HIGHLIGHT_CSS</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
  </span>

</h3>
<div class="language-python doc-signature highlight"><pre id="__code_0"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_0 > code"></button><code><span class="n">DEFAULT_HIGHLIGHT_CSS</span> <span class="o">=</span> <span class="s1">'fill:#fdff32'</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The default CSS to use for highlighting nodes.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h3 id="pydantic_graph.mermaid.StateDiagramDirection" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">StateDiagramDirection</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
  </span>

</h3>
<div class="language-python doc-signature highlight"><pre id="__code_1"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_1 > code"></button><code><span class="n">StateDiagramDirection</span> <span class="o">=</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Literal" href="https://docs.python.org/3/library/typing.html#typing.Literal">Literal</a></span><span class="p">[</span><span class="s1">'TB'</span><span class="p">,</span> <span class="s1">'LR'</span><span class="p">,</span> <span class="s1">'RL'</span><span class="p">,</span> <span class="s1">'BT'</span><span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Used to specify the direction of the state diagram generated by mermaid.</p>
<ul>
<li><code>'TB'</code>: Top to bottom, this is the default for mermaid charts.</li>
<li><code>'LR'</code>: Left to right</li>
<li><code>'RL'</code>: Right to left</li>
<li><code>'BT'</code>: Bottom to top</li>
</ul>
    </div>

</div>






<div class="doc doc-object doc-function">


<h3 id="pydantic_graph.mermaid.generate_code" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">generate_code</span>


</h3>
<div class="language-python doc-signature highlight"><pre id="__code_2"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_2 > code"></button><code><span class="nf">generate_code</span><span class="p">(</span>
    <span class="n">graph</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.graph.Graph" href="../graph/#pydantic_graph.graph.Graph">Graph</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a></span><span class="p">],</span>
    <span class="o">/</span><span class="p">,</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">start_node</span><span class="p">:</span> <span class="p">(</span>
        <span class="n"><a class="autorefs autorefs-external" title="collections.abc.Sequence" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence">Sequence</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.mermaid.NodeIdent" href="#pydantic_graph.mermaid.NodeIdent">NodeIdent</a></span><span class="p">]</span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.mermaid.NodeIdent" href="#pydantic_graph.mermaid.NodeIdent">NodeIdent</a></span> <span class="o">|</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">highlighted_nodes</span><span class="p">:</span> <span class="p">(</span>
        <span class="n"><a class="autorefs autorefs-external" title="collections.abc.Sequence" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence">Sequence</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.mermaid.NodeIdent" href="#pydantic_graph.mermaid.NodeIdent">NodeIdent</a></span><span class="p">]</span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.mermaid.NodeIdent" href="#pydantic_graph.mermaid.NodeIdent">NodeIdent</a></span> <span class="o">|</span> <span class="kc">None</span>
    <span class="p">)</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">highlight_css</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">=</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.mermaid.DEFAULT_HIGHLIGHT_CSS" href="#pydantic_graph.mermaid.DEFAULT_HIGHLIGHT_CSS">DEFAULT_HIGHLIGHT_CSS</a></span><span class="p">,</span>
    <span class="n">title</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">edge_labels</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="n">notes</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="n">direction</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.mermaid.StateDiagramDirection" href="#pydantic_graph.mermaid.StateDiagramDirection">StateDiagramDirection</a></span> <span class="o">|</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Generate <a href="https://mermaid.js.org/syntax/stateDiagram.html">Mermaid state diagram</a> code for a graph.</p>


<p><span class="doc-section-title">Parameters:</span></p>
    <div class="md-typeset__scrollwrap"><div class="md-typeset__table"><table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>graph</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_graph.graph.Graph" href="../graph/#pydantic_graph.graph.Graph">Graph</a>[<a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a>, <a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a>, <a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a>]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The graph to generate the image for.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>start_node</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" title="collections.abc.Sequence" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence">Sequence</a>[<a class="autorefs autorefs-internal" title="pydantic_graph.mermaid.NodeIdent" href="#pydantic_graph.mermaid.NodeIdent">NodeIdent</a>] | <a class="autorefs autorefs-internal" title="pydantic_graph.mermaid.NodeIdent" href="#pydantic_graph.mermaid.NodeIdent">NodeIdent</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Identifiers of nodes that start the graph.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>highlighted_nodes</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" title="collections.abc.Sequence" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence">Sequence</a>[<a class="autorefs autorefs-internal" title="pydantic_graph.mermaid.NodeIdent" href="#pydantic_graph.mermaid.NodeIdent">NodeIdent</a>] | <a class="autorefs autorefs-internal" title="pydantic_graph.mermaid.NodeIdent" href="#pydantic_graph.mermaid.NodeIdent">NodeIdent</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Identifiers of nodes to highlight.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>highlight_css</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>CSS to use for highlighting nodes.</p>
              </div>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_graph.mermaid.DEFAULT_HIGHLIGHT_CSS" href="#pydantic_graph.mermaid.DEFAULT_HIGHLIGHT_CSS">DEFAULT_HIGHLIGHT_CSS</a></code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>title</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The title of the diagram.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>edge_labels</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Whether to include edge labels in the diagram.</p>
              </div>
            </td>
            <td>
                  <code>True</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>notes</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Whether to include notes in the diagram.</p>
              </div>
            </td>
            <td>
                  <code>True</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>direction</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_graph.mermaid.StateDiagramDirection" href="#pydantic_graph.mermaid.StateDiagramDirection">StateDiagramDirection</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The direction of flow.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
      </tbody>
    </table></div></div>


    <p><span class="doc-section-title">Returns:</span></p>
    <div class="md-typeset__scrollwrap"><div class="md-typeset__table"><table>
      <thead>
        <tr>
          <th>Type</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The Mermaid code for the graph.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_graph/pydantic_graph/mermaid.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 41</span>
<span class="normal"> 42</span>
<span class="normal"> 43</span>
<span class="normal"> 44</span>
<span class="normal"> 45</span>
<span class="normal"> 46</span>
<span class="normal"> 47</span>
<span class="normal"> 48</span>
<span class="normal"> 49</span>
<span class="normal"> 50</span>
<span class="normal"> 51</span>
<span class="normal"> 52</span>
<span class="normal"> 53</span>
<span class="normal"> 54</span>
<span class="normal"> 55</span>
<span class="normal"> 56</span>
<span class="normal"> 57</span>
<span class="normal"> 58</span>
<span class="normal"> 59</span>
<span class="normal"> 60</span>
<span class="normal"> 61</span>
<span class="normal"> 62</span>
<span class="normal"> 63</span>
<span class="normal"> 64</span>
<span class="normal"> 65</span>
<span class="normal"> 66</span>
<span class="normal"> 67</span>
<span class="normal"> 68</span>
<span class="normal"> 69</span>
<span class="normal"> 70</span>
<span class="normal"> 71</span>
<span class="normal"> 72</span>
<span class="normal"> 73</span>
<span class="normal"> 74</span>
<span class="normal"> 75</span>
<span class="normal"> 76</span>
<span class="normal"> 77</span>
<span class="normal"> 78</span>
<span class="normal"> 79</span>
<span class="normal"> 80</span>
<span class="normal"> 81</span>
<span class="normal"> 82</span>
<span class="normal"> 83</span>
<span class="normal"> 84</span>
<span class="normal"> 85</span>
<span class="normal"> 86</span>
<span class="normal"> 87</span>
<span class="normal"> 88</span>
<span class="normal"> 89</span>
<span class="normal"> 90</span>
<span class="normal"> 91</span>
<span class="normal"> 92</span>
<span class="normal"> 93</span>
<span class="normal"> 94</span>
<span class="normal"> 95</span>
<span class="normal"> 96</span>
<span class="normal"> 97</span>
<span class="normal"> 98</span>
<span class="normal"> 99</span>
<span class="normal">100</span>
<span class="normal">101</span>
<span class="normal">102</span>
<span class="normal">103</span>
<span class="normal">104</span>
<span class="normal">105</span>
<span class="normal">106</span>
<span class="normal">107</span>
<span class="normal">108</span>
<span class="normal">109</span>
<span class="normal">110</span>
<span class="normal">111</span>
<span class="normal">112</span>
<span class="normal">113</span>
<span class="normal">114</span></pre></div></td><td class="code"><div><pre id="__code_3"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_3 > code"></button><code><span class="k">def</span><span class="w"> </span><span class="nf">generate_code</span><span class="p">(</span>  <span class="c1"># noqa: C901</span>
    <span class="n">graph</span><span class="p">:</span> <span class="n">Graph</span><span class="p">[</span><span class="n">Any</span><span class="p">,</span> <span class="n">Any</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span>
    <span class="o">/</span><span class="p">,</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">start_node</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">NodeIdent</span><span class="p">]</span> <span class="o">|</span> <span class="n">NodeIdent</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">highlighted_nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">NodeIdent</span><span class="p">]</span> <span class="o">|</span> <span class="n">NodeIdent</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">highlight_css</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">DEFAULT_HIGHLIGHT_CSS</span><span class="p">,</span>
    <span class="n">title</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">edge_labels</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="n">notes</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="n">direction</span><span class="p">:</span> <span class="n">StateDiagramDirection</span> <span class="o">|</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Generate [Mermaid state diagram](https://mermaid.js.org/syntax/stateDiagram.html) code for a graph.</span>

<span class="sd">    Args:</span>
<span class="sd">        graph: The graph to generate the image for.</span>
<span class="sd">        start_node: Identifiers of nodes that start the graph.</span>
<span class="sd">        highlighted_nodes: Identifiers of nodes to highlight.</span>
<span class="sd">        highlight_css: CSS to use for highlighting nodes.</span>
<span class="sd">        title: The title of the diagram.</span>
<span class="sd">        edge_labels: Whether to include edge labels in the diagram.</span>
<span class="sd">        notes: Whether to include notes in the diagram.</span>
<span class="sd">        direction: The direction of flow.</span>


<span class="sd">    Returns:</span>
<span class="sd">        The Mermaid code for the graph.</span>
<span class="sd">    """</span>
    <span class="n">start_node_ids</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">_node_ids</span><span class="p">(</span><span class="n">start_node</span> <span class="ow">or</span> <span class="p">()))</span>
    <span class="k">for</span> <span class="n">node_id</span> <span class="ow">in</span> <span class="n">start_node_ids</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">node_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">graph</span><span class="o">.</span><span class="n">node_defs</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">LookupError</span><span class="p">(</span><span class="sa">f</span><span class="s1">'Start node "</span><span class="si">{</span><span class="n">node_id</span><span class="si">}</span><span class="s1">" is not in the graph.'</span><span class="p">)</span>

    <span class="n">lines</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">if</span> <span class="n">title</span><span class="p">:</span>
        <span class="n">lines</span> <span class="o">=</span> <span class="p">[</span><span class="s1">'---'</span><span class="p">,</span> <span class="sa">f</span><span class="s1">'title: </span><span class="si">{</span><span class="n">title</span><span class="si">}</span><span class="s1">'</span><span class="p">,</span> <span class="s1">'---'</span><span class="p">]</span>
    <span class="n">lines</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s1">'stateDiagram-v2'</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">direction</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">lines</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s1">'  direction </span><span class="si">{</span><span class="n">direction</span><span class="si">}</span><span class="s1">'</span><span class="p">)</span>
    <span class="k">for</span> <span class="n">node_id</span><span class="p">,</span> <span class="n">node_def</span> <span class="ow">in</span> <span class="n">graph</span><span class="o">.</span><span class="n">node_defs</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
        <span class="c1"># we use round brackets (rounded box) for nodes other than the start and end</span>
        <span class="k">if</span> <span class="n">node_id</span> <span class="ow">in</span> <span class="n">start_node_ids</span><span class="p">:</span>
            <span class="n">lines</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s1">'  [*] --&gt; </span><span class="si">{</span><span class="n">node_id</span><span class="si">}</span><span class="s1">'</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">node_def</span><span class="o">.</span><span class="n">returns_base_node</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">next_node_id</span> <span class="ow">in</span> <span class="n">graph</span><span class="o">.</span><span class="n">node_defs</span><span class="p">:</span>
                <span class="n">lines</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s1">'  </span><span class="si">{</span><span class="n">node_id</span><span class="si">}</span><span class="s1"> --&gt; </span><span class="si">{</span><span class="n">next_node_id</span><span class="si">}</span><span class="s1">'</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">next_node_id</span><span class="p">,</span> <span class="n">edge</span> <span class="ow">in</span> <span class="n">node_def</span><span class="o">.</span><span class="n">next_node_edges</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
                <span class="n">line</span> <span class="o">=</span> <span class="sa">f</span><span class="s1">'  </span><span class="si">{</span><span class="n">node_id</span><span class="si">}</span><span class="s1"> --&gt; </span><span class="si">{</span><span class="n">next_node_id</span><span class="si">}</span><span class="s1">'</span>
                <span class="k">if</span> <span class="n">edge_labels</span> <span class="ow">and</span> <span class="n">edge</span><span class="o">.</span><span class="n">label</span><span class="p">:</span>
                    <span class="n">line</span> <span class="o">+=</span> <span class="sa">f</span><span class="s1">': </span><span class="si">{</span><span class="n">edge</span><span class="o">.</span><span class="n">label</span><span class="si">}</span><span class="s1">'</span>
                <span class="n">lines</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">line</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">end_edge</span> <span class="o">:=</span> <span class="n">node_def</span><span class="o">.</span><span class="n">end_edge</span><span class="p">:</span>
            <span class="n">line</span> <span class="o">=</span> <span class="sa">f</span><span class="s1">'  </span><span class="si">{</span><span class="n">node_id</span><span class="si">}</span><span class="s1"> --&gt; [*]'</span>
            <span class="k">if</span> <span class="n">edge_labels</span> <span class="ow">and</span> <span class="n">end_edge</span><span class="o">.</span><span class="n">label</span><span class="p">:</span>
                <span class="n">line</span> <span class="o">+=</span> <span class="sa">f</span><span class="s1">': </span><span class="si">{</span><span class="n">end_edge</span><span class="o">.</span><span class="n">label</span><span class="si">}</span><span class="s1">'</span>
            <span class="n">lines</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">line</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">notes</span> <span class="ow">and</span> <span class="n">node_def</span><span class="o">.</span><span class="n">note</span><span class="p">:</span>
            <span class="n">lines</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s1">'  note right of </span><span class="si">{</span><span class="n">node_id</span><span class="si">}</span><span class="s1">'</span><span class="p">)</span>
            <span class="c1"># mermaid doesn't like multiple paragraphs in a note, and shows if so</span>
            <span class="n">clean_docs</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="s1">'</span><span class="se">\n</span><span class="s1">{2,}'</span><span class="p">,</span> <span class="s1">'</span><span class="se">\n</span><span class="s1">'</span><span class="p">,</span> <span class="n">node_def</span><span class="o">.</span><span class="n">note</span><span class="p">)</span>
            <span class="n">lines</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">indent</span><span class="p">(</span><span class="n">clean_docs</span><span class="p">,</span> <span class="s1">'    '</span><span class="p">))</span>
            <span class="n">lines</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s1">'  end note'</span><span class="p">)</span>

    <span class="k">if</span> <span class="n">highlighted_nodes</span><span class="p">:</span>
        <span class="n">lines</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s1">''</span><span class="p">)</span>
        <span class="n">lines</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s1">'classDef highlighted </span><span class="si">{</span><span class="n">highlight_css</span><span class="si">}</span><span class="s1">'</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">node_id</span> <span class="ow">in</span> <span class="n">_node_ids</span><span class="p">(</span><span class="n">highlighted_nodes</span><span class="p">):</span>
            <span class="k">if</span> <span class="n">node_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">graph</span><span class="o">.</span><span class="n">node_defs</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">LookupError</span><span class="p">(</span><span class="sa">f</span><span class="s1">'Highlighted node "</span><span class="si">{</span><span class="n">node_id</span><span class="si">}</span><span class="s1">" is not in the graph.'</span><span class="p">)</span>
            <span class="n">lines</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s1">'class </span><span class="si">{</span><span class="n">node_id</span><span class="si">}</span><span class="s1"> highlighted'</span><span class="p">)</span>

    <span class="k">return</span> <span class="s1">'</span><span class="se">\n</span><span class="s1">'</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">lines</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>










<div class="doc doc-object doc-function">


<h3 id="pydantic_graph.mermaid.request_image" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">request_image</span>


</h3>
<div class="language-python doc-signature highlight"><pre id="__code_4"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_4 > code"></button><code><span class="nf">request_image</span><span class="p">(</span>
    <span class="n">graph</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.graph.Graph" href="../graph/#pydantic_graph.graph.Graph">Graph</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a></span><span class="p">],</span>
    <span class="o">/</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="typing_extensions.Unpack" href="https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Unpack">Unpack</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.mermaid.MermaidConfig" href="#pydantic_graph.mermaid.MermaidConfig">MermaidConfig</a></span><span class="p">],</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#bytes">bytes</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Generate an image of a Mermaid diagram using <a href="https://mermaid.ink">mermaid.ink</a>.</p>


<p><span class="doc-section-title">Parameters:</span></p>
    <div class="md-typeset__scrollwrap"><div class="md-typeset__table"><table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>graph</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_graph.graph.Graph" href="../graph/#pydantic_graph.graph.Graph">Graph</a>[<a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a>, <a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a>, <a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a>]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The graph to generate the image for.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>**kwargs</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" title="typing_extensions.Unpack" href="https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Unpack">Unpack</a>[<a class="autorefs autorefs-internal" title="pydantic_graph.mermaid.MermaidConfig" href="#pydantic_graph.mermaid.MermaidConfig">MermaidConfig</a>]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Additional parameters to configure mermaid chart generation.</p>
              </div>
            </td>
            <td>
                  <code>{}</code>
            </td>
          </tr>
      </tbody>
    </table></div></div>


    <p><span class="doc-section-title">Returns:</span></p>
    <div class="md-typeset__scrollwrap"><div class="md-typeset__table"><table>
      <thead>
        <tr>
          <th>Type</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#bytes">bytes</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The image data.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_graph/pydantic_graph/mermaid.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">133</span>
<span class="normal">134</span>
<span class="normal">135</span>
<span class="normal">136</span>
<span class="normal">137</span>
<span class="normal">138</span>
<span class="normal">139</span>
<span class="normal">140</span>
<span class="normal">141</span>
<span class="normal">142</span>
<span class="normal">143</span>
<span class="normal">144</span>
<span class="normal">145</span>
<span class="normal">146</span>
<span class="normal">147</span>
<span class="normal">148</span>
<span class="normal">149</span>
<span class="normal">150</span>
<span class="normal">151</span>
<span class="normal">152</span>
<span class="normal">153</span>
<span class="normal">154</span>
<span class="normal">155</span>
<span class="normal">156</span>
<span class="normal">157</span>
<span class="normal">158</span>
<span class="normal">159</span>
<span class="normal">160</span>
<span class="normal">161</span>
<span class="normal">162</span>
<span class="normal">163</span>
<span class="normal">164</span>
<span class="normal">165</span>
<span class="normal">166</span>
<span class="normal">167</span>
<span class="normal">168</span>
<span class="normal">169</span>
<span class="normal">170</span>
<span class="normal">171</span>
<span class="normal">172</span>
<span class="normal">173</span>
<span class="normal">174</span>
<span class="normal">175</span>
<span class="normal">176</span>
<span class="normal">177</span>
<span class="normal">178</span>
<span class="normal">179</span>
<span class="normal">180</span>
<span class="normal">181</span>
<span class="normal">182</span>
<span class="normal">183</span>
<span class="normal">184</span>
<span class="normal">185</span>
<span class="normal">186</span>
<span class="normal">187</span>
<span class="normal">188</span>
<span class="normal">189</span>
<span class="normal">190</span>
<span class="normal">191</span>
<span class="normal">192</span>
<span class="normal">193</span>
<span class="normal">194</span>
<span class="normal">195</span></pre></div></td><td class="code"><div><pre id="__code_5"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_5 > code"></button><code><span class="k">def</span><span class="w"> </span><span class="nf">request_image</span><span class="p">(</span>
    <span class="n">graph</span><span class="p">:</span> <span class="n">Graph</span><span class="p">[</span><span class="n">Any</span><span class="p">,</span> <span class="n">Any</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span>
    <span class="o">/</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Unpack</span><span class="p">[</span><span class="n">MermaidConfig</span><span class="p">],</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bytes</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Generate an image of a Mermaid diagram using [mermaid.ink](https://mermaid.ink).</span>

<span class="sd">    Args:</span>
<span class="sd">        graph: The graph to generate the image for.</span>
<span class="sd">        **kwargs: Additional parameters to configure mermaid chart generation.</span>

<span class="sd">    Returns:</span>
<span class="sd">        The image data.</span>
<span class="sd">    """</span>
    <span class="n">code</span> <span class="o">=</span> <span class="n">generate_code</span><span class="p">(</span>
        <span class="n">graph</span><span class="p">,</span>
        <span class="n">start_node</span><span class="o">=</span><span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'start_node'</span><span class="p">),</span>
        <span class="n">highlighted_nodes</span><span class="o">=</span><span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'highlighted_nodes'</span><span class="p">),</span>
        <span class="n">highlight_css</span><span class="o">=</span><span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'highlight_css'</span><span class="p">,</span> <span class="n">DEFAULT_HIGHLIGHT_CSS</span><span class="p">),</span>
        <span class="n">title</span><span class="o">=</span><span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'title'</span><span class="p">),</span>
        <span class="n">edge_labels</span><span class="o">=</span><span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'edge_labels'</span><span class="p">,</span> <span class="kc">True</span><span class="p">),</span>
        <span class="n">notes</span><span class="o">=</span><span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'notes'</span><span class="p">,</span> <span class="kc">True</span><span class="p">),</span>
        <span class="n">direction</span><span class="o">=</span><span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'direction'</span><span class="p">),</span>
    <span class="p">)</span>
    <span class="n">code_base64</span> <span class="o">=</span> <span class="n">base64</span><span class="o">.</span><span class="n">b64encode</span><span class="p">(</span><span class="n">code</span><span class="o">.</span><span class="n">encode</span><span class="p">())</span><span class="o">.</span><span class="n">decode</span><span class="p">()</span>

    <span class="n">params</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span> <span class="o">|</span> <span class="nb">float</span><span class="p">]</span> <span class="o">=</span> <span class="p">{}</span>
    <span class="k">if</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'image_type'</span><span class="p">)</span> <span class="o">==</span> <span class="s1">'pdf'</span><span class="p">:</span>
        <span class="n">url</span> <span class="o">=</span> <span class="sa">f</span><span class="s1">'https://mermaid.ink/pdf/</span><span class="si">{</span><span class="n">code_base64</span><span class="si">}</span><span class="s1">'</span>
        <span class="k">if</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'pdf_fit'</span><span class="p">):</span>
            <span class="n">params</span><span class="p">[</span><span class="s1">'fit'</span><span class="p">]</span> <span class="o">=</span> <span class="s1">''</span>
        <span class="k">if</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'pdf_landscape'</span><span class="p">):</span>
            <span class="n">params</span><span class="p">[</span><span class="s1">'landscape'</span><span class="p">]</span> <span class="o">=</span> <span class="s1">''</span>
        <span class="k">if</span> <span class="n">pdf_paper</span> <span class="o">:=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'pdf_paper'</span><span class="p">):</span>
            <span class="n">params</span><span class="p">[</span><span class="s1">'paper'</span><span class="p">]</span> <span class="o">=</span> <span class="n">pdf_paper</span>
    <span class="k">elif</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'image_type'</span><span class="p">)</span> <span class="o">==</span> <span class="s1">'svg'</span><span class="p">:</span>
        <span class="n">url</span> <span class="o">=</span> <span class="sa">f</span><span class="s1">'https://mermaid.ink/svg/</span><span class="si">{</span><span class="n">code_base64</span><span class="si">}</span><span class="s1">'</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">url</span> <span class="o">=</span> <span class="sa">f</span><span class="s1">'https://mermaid.ink/img/</span><span class="si">{</span><span class="n">code_base64</span><span class="si">}</span><span class="s1">'</span>

        <span class="k">if</span> <span class="n">image_type</span> <span class="o">:=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'image_type'</span><span class="p">):</span>
            <span class="n">params</span><span class="p">[</span><span class="s1">'type'</span><span class="p">]</span> <span class="o">=</span> <span class="n">image_type</span>

    <span class="k">if</span> <span class="n">background_color</span> <span class="o">:=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'background_color'</span><span class="p">):</span>
        <span class="n">params</span><span class="p">[</span><span class="s1">'bgColor'</span><span class="p">]</span> <span class="o">=</span> <span class="n">background_color</span>
    <span class="k">if</span> <span class="n">theme</span> <span class="o">:=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'theme'</span><span class="p">):</span>
        <span class="n">params</span><span class="p">[</span><span class="s1">'theme'</span><span class="p">]</span> <span class="o">=</span> <span class="n">theme</span>
    <span class="k">if</span> <span class="n">width</span> <span class="o">:=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'width'</span><span class="p">):</span>
        <span class="n">params</span><span class="p">[</span><span class="s1">'width'</span><span class="p">]</span> <span class="o">=</span> <span class="n">width</span>
    <span class="k">if</span> <span class="n">height</span> <span class="o">:=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'height'</span><span class="p">):</span>
        <span class="n">params</span><span class="p">[</span><span class="s1">'height'</span><span class="p">]</span> <span class="o">=</span> <span class="n">height</span>
    <span class="k">if</span> <span class="n">scale</span> <span class="o">:=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'scale'</span><span class="p">):</span>
        <span class="n">params</span><span class="p">[</span><span class="s1">'scale'</span><span class="p">]</span> <span class="o">=</span> <span class="n">scale</span>

    <span class="n">httpx_client</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'httpx_client'</span><span class="p">)</span> <span class="ow">or</span> <span class="n">httpx</span><span class="o">.</span><span class="n">Client</span><span class="p">()</span>
    <span class="n">response</span> <span class="o">=</span> <span class="n">httpx_client</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">url</span><span class="p">,</span> <span class="n">params</span><span class="o">=</span><span class="n">params</span><span class="p">)</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="n">response</span><span class="o">.</span><span class="n">is_success</span><span class="p">:</span>
        <span class="k">raise</span> <span class="n">httpx</span><span class="o">.</span><span class="n">HTTPStatusError</span><span class="p">(</span>
            <span class="sa">f</span><span class="s1">'</span><span class="si">{</span><span class="n">response</span><span class="o">.</span><span class="n">status_code</span><span class="si">}</span><span class="s1"> error generating image:</span><span class="se">\n</span><span class="si">{</span><span class="n">response</span><span class="o">.</span><span class="n">text</span><span class="si">}</span><span class="s1">'</span><span class="p">,</span>
            <span class="n">request</span><span class="o">=</span><span class="n">response</span><span class="o">.</span><span class="n">request</span><span class="p">,</span>
            <span class="n">response</span><span class="o">=</span><span class="n">response</span><span class="p">,</span>
        <span class="p">)</span>
    <span class="k">return</span> <span class="n">response</span><span class="o">.</span><span class="n">content</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h3 id="pydantic_graph.mermaid.save_image" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">save_image</span>


</h3>
<div class="language-python doc-signature highlight"><pre id="__code_6"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_6 > code"></button><code><span class="nf">save_image</span><span class="p">(</span>
    <span class="n">path</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="pathlib.Path" href="https://docs.python.org/3/library/pathlib.html#pathlib.Path">Path</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span><span class="p">,</span>
    <span class="n">graph</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.graph.Graph" href="../graph/#pydantic_graph.graph.Graph">Graph</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a></span><span class="p">],</span>
    <span class="o">/</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="typing_extensions.Unpack" href="https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Unpack">Unpack</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.mermaid.MermaidConfig" href="#pydantic_graph.mermaid.MermaidConfig">MermaidConfig</a></span><span class="p">],</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Generate an image of a Mermaid diagram using <a href="https://mermaid.ink">mermaid.ink</a> and save it to a local file.</p>


<p><span class="doc-section-title">Parameters:</span></p>
    <div class="md-typeset__scrollwrap"><div class="md-typeset__table"><table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>path</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" title="pathlib.Path" href="https://docs.python.org/3/library/pathlib.html#pathlib.Path">Path</a> | <a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The path to save the image to.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>graph</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_graph.graph.Graph" href="../graph/#pydantic_graph.graph.Graph">Graph</a>[<a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a>, <a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a>, <a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a>]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The graph to generate the image for.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>**kwargs</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" title="typing_extensions.Unpack" href="https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Unpack">Unpack</a>[<a class="autorefs autorefs-internal" title="pydantic_graph.mermaid.MermaidConfig" href="#pydantic_graph.mermaid.MermaidConfig">MermaidConfig</a>]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Additional parameters to configure mermaid chart generation.</p>
              </div>
            </td>
            <td>
                  <code>{}</code>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_graph/pydantic_graph/mermaid.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">198</span>
<span class="normal">199</span>
<span class="normal">200</span>
<span class="normal">201</span>
<span class="normal">202</span>
<span class="normal">203</span>
<span class="normal">204</span>
<span class="normal">205</span>
<span class="normal">206</span>
<span class="normal">207</span>
<span class="normal">208</span>
<span class="normal">209</span>
<span class="normal">210</span>
<span class="normal">211</span>
<span class="normal">212</span>
<span class="normal">213</span>
<span class="normal">214</span>
<span class="normal">215</span>
<span class="normal">216</span>
<span class="normal">217</span>
<span class="normal">218</span>
<span class="normal">219</span>
<span class="normal">220</span>
<span class="normal">221</span></pre></div></td><td class="code"><div><pre id="__code_7"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_7 > code"></button><code tabindex="0"><span class="k">def</span><span class="w"> </span><span class="nf">save_image</span><span class="p">(</span>
    <span class="n">path</span><span class="p">:</span> <span class="n">Path</span> <span class="o">|</span> <span class="nb">str</span><span class="p">,</span>
    <span class="n">graph</span><span class="p">:</span> <span class="n">Graph</span><span class="p">[</span><span class="n">Any</span><span class="p">,</span> <span class="n">Any</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span>
    <span class="o">/</span><span class="p">,</span>
    <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Unpack</span><span class="p">[</span><span class="n">MermaidConfig</span><span class="p">],</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Generate an image of a Mermaid diagram using [mermaid.ink](https://mermaid.ink) and save it to a local file.</span>

<span class="sd">    Args:</span>
<span class="sd">        path: The path to save the image to.</span>
<span class="sd">        graph: The graph to generate the image for.</span>
<span class="sd">        **kwargs: Additional parameters to configure mermaid chart generation.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">path</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
        <span class="n">path</span> <span class="o">=</span> <span class="n">Path</span><span class="p">(</span><span class="n">path</span><span class="p">)</span>

    <span class="k">if</span> <span class="s1">'image_type'</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="p">:</span>
        <span class="n">ext</span> <span class="o">=</span> <span class="n">path</span><span class="o">.</span><span class="n">suffix</span><span class="o">.</span><span class="n">lower</span><span class="p">()[</span><span class="mi">1</span><span class="p">:]</span>
        <span class="c1"># no need to check for .jpeg/.jpg, as it is the default</span>
        <span class="k">if</span> <span class="n">ext</span> <span class="ow">in</span> <span class="p">(</span><span class="s1">'png'</span><span class="p">,</span> <span class="s1">'webp'</span><span class="p">,</span> <span class="s1">'svg'</span><span class="p">,</span> <span class="s1">'pdf'</span><span class="p">):</span>
            <span class="n">kwargs</span><span class="p">[</span><span class="s1">'image_type'</span><span class="p">]</span> <span class="o">=</span> <span class="n">ext</span>

    <span class="n">image_data</span> <span class="o">=</span> <span class="n">request_image</span><span class="p">(</span><span class="n">graph</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
    <span class="n">path</span><span class="o">.</span><span class="n">write_bytes</span><span class="p">(</span><span class="n">image_data</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-class">



<h3 id="pydantic_graph.mermaid.MermaidConfig" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">MermaidConfig</span>


</h3>


    <div class="doc doc-contents ">
            <p class="doc doc-class-bases">
              Bases: <code><a class="autorefs autorefs-external" title="typing_extensions.TypedDict" href="https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypedDict">TypedDict</a></code></p>


        <p>Parameters to configure mermaid chart generation.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_graph/pydantic_graph/mermaid.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">224</span>
<span class="normal">225</span>
<span class="normal">226</span>
<span class="normal">227</span>
<span class="normal">228</span>
<span class="normal">229</span>
<span class="normal">230</span>
<span class="normal">231</span>
<span class="normal">232</span>
<span class="normal">233</span>
<span class="normal">234</span>
<span class="normal">235</span>
<span class="normal">236</span>
<span class="normal">237</span>
<span class="normal">238</span>
<span class="normal">239</span>
<span class="normal">240</span>
<span class="normal">241</span>
<span class="normal">242</span>
<span class="normal">243</span>
<span class="normal">244</span>
<span class="normal">245</span>
<span class="normal">246</span>
<span class="normal">247</span>
<span class="normal">248</span>
<span class="normal">249</span>
<span class="normal">250</span>
<span class="normal">251</span>
<span class="normal">252</span>
<span class="normal">253</span>
<span class="normal">254</span>
<span class="normal">255</span>
<span class="normal">256</span>
<span class="normal">257</span>
<span class="normal">258</span>
<span class="normal">259</span>
<span class="normal">260</span>
<span class="normal">261</span>
<span class="normal">262</span>
<span class="normal">263</span>
<span class="normal">264</span>
<span class="normal">265</span>
<span class="normal">266</span>
<span class="normal">267</span>
<span class="normal">268</span>
<span class="normal">269</span>
<span class="normal">270</span>
<span class="normal">271</span></pre></div></td><td class="code"><div><pre id="__code_8"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_8 > code"></button><code tabindex="0"><span class="k">class</span><span class="w"> </span><span class="nc">MermaidConfig</span><span class="p">(</span><span class="n">TypedDict</span><span class="p">,</span> <span class="n">total</span><span class="o">=</span><span class="kc">False</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Parameters to configure mermaid chart generation."""</span>

    <span class="n">start_node</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">NodeIdent</span><span class="p">]</span> <span class="o">|</span> <span class="n">NodeIdent</span>
<span class="w">    </span><span class="sd">"""Identifiers of nodes that start the graph."""</span>
    <span class="n">highlighted_nodes</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">NodeIdent</span><span class="p">]</span> <span class="o">|</span> <span class="n">NodeIdent</span>
<span class="w">    </span><span class="sd">"""Identifiers of nodes to highlight."""</span>
    <span class="n">highlight_css</span><span class="p">:</span> <span class="nb">str</span>
<span class="w">    </span><span class="sd">"""CSS to use for highlighting nodes."""</span>
    <span class="n">title</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span>
<span class="w">    </span><span class="sd">"""The title of the diagram."""</span>
    <span class="n">edge_labels</span><span class="p">:</span> <span class="nb">bool</span>
<span class="w">    </span><span class="sd">"""Whether to include edge labels in the diagram."""</span>
    <span class="n">notes</span><span class="p">:</span> <span class="nb">bool</span>
<span class="w">    </span><span class="sd">"""Whether to include notes on nodes in the diagram, defaults to true."""</span>
    <span class="n">image_type</span><span class="p">:</span> <span class="n">Literal</span><span class="p">[</span><span class="s1">'jpeg'</span><span class="p">,</span> <span class="s1">'png'</span><span class="p">,</span> <span class="s1">'webp'</span><span class="p">,</span> <span class="s1">'svg'</span><span class="p">,</span> <span class="s1">'pdf'</span><span class="p">]</span>
<span class="w">    </span><span class="sd">"""The image type to generate. If unspecified, the default behavior is `'jpeg'`."""</span>
    <span class="n">pdf_fit</span><span class="p">:</span> <span class="nb">bool</span>
<span class="w">    </span><span class="sd">"""When using image_type='pdf', whether to fit the diagram to the PDF page."""</span>
    <span class="n">pdf_landscape</span><span class="p">:</span> <span class="nb">bool</span>
<span class="w">    </span><span class="sd">"""When using image_type='pdf', whether to use landscape orientation for the PDF.</span>

<span class="sd">    This has no effect if using `pdf_fit`.</span>
<span class="sd">    """</span>
    <span class="n">pdf_paper</span><span class="p">:</span> <span class="n">Literal</span><span class="p">[</span><span class="s1">'letter'</span><span class="p">,</span> <span class="s1">'legal'</span><span class="p">,</span> <span class="s1">'tabloid'</span><span class="p">,</span> <span class="s1">'ledger'</span><span class="p">,</span> <span class="s1">'a0'</span><span class="p">,</span> <span class="s1">'a1'</span><span class="p">,</span> <span class="s1">'a2'</span><span class="p">,</span> <span class="s1">'a3'</span><span class="p">,</span> <span class="s1">'a4'</span><span class="p">,</span> <span class="s1">'a5'</span><span class="p">,</span> <span class="s1">'a6'</span><span class="p">]</span>
<span class="w">    </span><span class="sd">"""When using image_type='pdf', the paper size of the PDF."""</span>
    <span class="n">background_color</span><span class="p">:</span> <span class="nb">str</span>
<span class="w">    </span><span class="sd">"""The background color of the diagram.</span>

<span class="sd">    If None, the default transparent background is used. The color value is interpreted as a hexadecimal color</span>
<span class="sd">    code by default (and should not have a leading '#'), but you can also use named colors by prefixing the</span>
<span class="sd">    value with `'!'`. For example, valid choices include `background_color='!white'` or `background_color='FF0000'`.</span>
<span class="sd">    """</span>
    <span class="n">theme</span><span class="p">:</span> <span class="n">Literal</span><span class="p">[</span><span class="s1">'default'</span><span class="p">,</span> <span class="s1">'neutral'</span><span class="p">,</span> <span class="s1">'dark'</span><span class="p">,</span> <span class="s1">'forest'</span><span class="p">]</span>
<span class="w">    </span><span class="sd">"""The theme of the diagram. Defaults to 'default'."""</span>
    <span class="n">width</span><span class="p">:</span> <span class="nb">int</span>
<span class="w">    </span><span class="sd">"""The width of the diagram."""</span>
    <span class="n">height</span><span class="p">:</span> <span class="nb">int</span>
<span class="w">    </span><span class="sd">"""The height of the diagram."""</span>
    <span class="n">scale</span><span class="p">:</span> <span class="n">Annotated</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="n">Ge</span><span class="p">(</span><span class="mi">1</span><span class="p">),</span> <span class="n">Le</span><span class="p">(</span><span class="mi">3</span><span class="p">)]</span>
<span class="w">    </span><span class="sd">"""The scale of the diagram.</span>

<span class="sd">    The scale must be a number between 1 and 3, and you can only set a scale if one or both of width and height are set.</span>
<span class="sd">    """</span>
    <span class="n">httpx_client</span><span class="p">:</span> <span class="n">httpx</span><span class="o">.</span><span class="n">Client</span>
<span class="w">    </span><span class="sd">"""An HTTPX client to use for requests, mostly for testing purposes."""</span>
    <span class="n">direction</span><span class="p">:</span> <span class="n">StateDiagramDirection</span>
<span class="w">    </span><span class="sd">"""The direction of the state diagram."""</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-attribute">



<h4 id="pydantic_graph.mermaid.MermaidConfig.start_node" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">start_node</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_9"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_9 > code"></button><code><span class="n">start_node</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="collections.abc.Sequence" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence">Sequence</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.mermaid.NodeIdent" href="#pydantic_graph.mermaid.NodeIdent">NodeIdent</a></span><span class="p">]</span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.mermaid.NodeIdent" href="#pydantic_graph.mermaid.NodeIdent">NodeIdent</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Identifiers of nodes that start the graph.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_graph.mermaid.MermaidConfig.highlighted_nodes" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">highlighted_nodes</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_10"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_10 > code"></button><code><span class="n">highlighted_nodes</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="collections.abc.Sequence" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence">Sequence</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.mermaid.NodeIdent" href="#pydantic_graph.mermaid.NodeIdent">NodeIdent</a></span><span class="p">]</span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.mermaid.NodeIdent" href="#pydantic_graph.mermaid.NodeIdent">NodeIdent</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Identifiers of nodes to highlight.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_graph.mermaid.MermaidConfig.highlight_css" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">highlight_css</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_11"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_11 > code"></button><code><span class="n">highlight_css</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>CSS to use for highlighting nodes.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_graph.mermaid.MermaidConfig.title" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">title</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_12"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_12 > code"></button><code><span class="n">title</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The title of the diagram.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_graph.mermaid.MermaidConfig.edge_labels" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">edge_labels</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_13"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_13 > code"></button><code><span class="n">edge_labels</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Whether to include edge labels in the diagram.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_graph.mermaid.MermaidConfig.notes" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">notes</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_14"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_14 > code"></button><code><span class="n">notes</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Whether to include notes on nodes in the diagram, defaults to true.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_graph.mermaid.MermaidConfig.image_type" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">image_type</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_15"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_15 > code"></button><code><span class="n">image_type</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Literal" href="https://docs.python.org/3/library/typing.html#typing.Literal">Literal</a></span><span class="p">[</span><span class="s1">'jpeg'</span><span class="p">,</span> <span class="s1">'png'</span><span class="p">,</span> <span class="s1">'webp'</span><span class="p">,</span> <span class="s1">'svg'</span><span class="p">,</span> <span class="s1">'pdf'</span><span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The image type to generate. If unspecified, the default behavior is <code>'jpeg'</code>.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_graph.mermaid.MermaidConfig.pdf_fit" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">pdf_fit</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_16"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_16 > code"></button><code><span class="n">pdf_fit</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>When using image_type='pdf', whether to fit the diagram to the PDF page.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_graph.mermaid.MermaidConfig.pdf_landscape" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">pdf_landscape</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_17"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_17 > code"></button><code><span class="n">pdf_landscape</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>When using image_type='pdf', whether to use landscape orientation for the PDF.</p>
<p>This has no effect if using <code>pdf_fit</code>.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_graph.mermaid.MermaidConfig.pdf_paper" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">pdf_paper</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_18"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_18 > code"></button><code><span class="n">pdf_paper</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Literal" href="https://docs.python.org/3/library/typing.html#typing.Literal">Literal</a></span><span class="p">[</span>
    <span class="s2">"letter"</span><span class="p">,</span>
    <span class="s2">"legal"</span><span class="p">,</span>
    <span class="s2">"tabloid"</span><span class="p">,</span>
    <span class="s2">"ledger"</span><span class="p">,</span>
    <span class="s2">"a0"</span><span class="p">,</span>
    <span class="s2">"a1"</span><span class="p">,</span>
    <span class="s2">"a2"</span><span class="p">,</span>
    <span class="s2">"a3"</span><span class="p">,</span>
    <span class="s2">"a4"</span><span class="p">,</span>
    <span class="s2">"a5"</span><span class="p">,</span>
    <span class="s2">"a6"</span><span class="p">,</span>
<span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>When using image_type='pdf', the paper size of the PDF.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_graph.mermaid.MermaidConfig.background_color" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">background_color</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_19"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_19 > code"></button><code><span class="n">background_color</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The background color of the diagram.</p>
<p>If None, the default transparent background is used. The color value is interpreted as a hexadecimal color
code by default (and should not have a leading '#'), but you can also use named colors by prefixing the
value with <code>'!'</code>. For example, valid choices include <code>background_color='!white'</code> or <code>background_color='FF0000'</code>.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_graph.mermaid.MermaidConfig.theme" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">theme</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_20"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_20 > code"></button><code><span class="n">theme</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Literal" href="https://docs.python.org/3/library/typing.html#typing.Literal">Literal</a></span><span class="p">[</span><span class="s1">'default'</span><span class="p">,</span> <span class="s1">'neutral'</span><span class="p">,</span> <span class="s1">'dark'</span><span class="p">,</span> <span class="s1">'forest'</span><span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The theme of the diagram. Defaults to 'default'.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_graph.mermaid.MermaidConfig.width" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">width</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_21"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_21 > code"></button><code><span class="n">width</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#int">int</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The width of the diagram.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_graph.mermaid.MermaidConfig.height" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">height</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_22"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_22 > code"></button><code><span class="n">height</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#int">int</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The height of the diagram.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_graph.mermaid.MermaidConfig.scale" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">scale</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_23"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_23 > code"></button><code><span class="n">scale</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Annotated" href="https://docs.python.org/3/library/typing.html#typing.Annotated">Annotated</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#float">float</a></span><span class="p">,</span> <span class="n"><span title="annotated_types.Ge">Ge</span></span><span class="p">(</span><span class="mi">1</span><span class="p">),</span> <span class="n"><span title="annotated_types.Le">Le</span></span><span class="p">(</span><span class="mi">3</span><span class="p">)]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The scale of the diagram.</p>
<p>The scale must be a number between 1 and 3, and you can only set a scale if one or both of width and height are set.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_graph.mermaid.MermaidConfig.httpx_client" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">httpx_client</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_24"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_24 > code"></button><code><span class="n">httpx_client</span><span class="p">:</span> <span class="n"><span title="httpx.Client">Client</span></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>An HTTPX client to use for requests, mostly for testing purposes.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_graph.mermaid.MermaidConfig.direction" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">direction</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_25"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_25 > code"></button><code><span class="n">direction</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_graph.mermaid.StateDiagramDirection" href="#pydantic_graph.mermaid.StateDiagramDirection">StateDiagramDirection</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The direction of the state diagram.</p>
    </div>

</div>




  </div>

    </div>

</div>






<div class="doc doc-object doc-attribute">



<h3 id="pydantic_graph.mermaid.NodeIdent" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">NodeIdent</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
  </span>

</h3>
<div class="language-python doc-signature highlight"><pre id="__code_26"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_26 > code"></button><code><span class="n">NodeIdent</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="typing_extensions.TypeAlias" href="https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypeAlias">TypeAlias</a></span> <span class="o">=</span> <span class="p">(</span>
    <span class="s2">"type[BaseNode[Any, Any, Any]] | BaseNode[Any, Any, Any] | str"</span>
<span class="p">)</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>A type alias for a node identifier.</p>
<p>This can be:</p>
<ul>
<li>A node instance (instance of a subclass of <a class="autorefs autorefs-internal" href="../nodes/#pydantic_graph.nodes.BaseNode"><code>BaseNode</code></a>).</li>
<li>A node class (subclass of <a class="autorefs autorefs-internal" href="../nodes/#pydantic_graph.nodes.BaseNode"><code>BaseNode</code></a>).</li>
<li>A string representing the node ID.</li>
</ul>
    </div>

</div>




  </div>

    </div>

</div>







  
  






                
              </article>
            </div>
          
          
  <script>var tabs=__md_get("__tabs");if(Array.isArray(tabs))e:for(var set of document.querySelectorAll(".tabbed-set")){var labels=set.querySelector(".tabbed-labels");for(var tab of tabs)for(var label of labels.getElementsByTagName("label"))if(label.innerText.trim()===tab){var input=document.getElementById(label.htmlFor);input.checked=!0;continue e}}</script>

<script>var target=document.getElementById(location.hash.slice(1));target&&target.name&&(target.checked=target.name.startsWith("__tabbed_"))</script>
        </div>
        
      </main>
      
        <footer class="md-footer">
  
  <div class="md-footer-meta md-typeset">
    <div class="md-footer-meta__inner md-grid">
      <div class="md-copyright">
  
    <div class="md-copyright__highlight">
      © Pydantic Services Inc. 2024 to present
    </div>
  
  
</div>
      
    </div>
  </div>
</footer>
      
    </div>
    <div class="md-dialog" data-md-component="dialog">
      <div class="md-dialog__inner md-typeset"></div>
    </div>
    
    
    <script id="__config" type="application/json">{"base": "../../..", "features": ["search.suggest", "search.highlight", "content.tabs.link", "content.code.annotate", "content.code.copy", "content.code.select", "navigation.path", "navigation.indexes", "navigation.sections", "navigation.tracking", "toc.follow"], "search": "../../../assets/javascripts/workers/search.f8cc74c7.min.js", "translations": {"clipboard.copied": "Copied to clipboard", "clipboard.copy": "Copy to clipboard", "search.result.more.one": "1 more on this page", "search.result.more.other": "# more on this page", "search.result.none": "No matching documents", "search.result.one": "1 matching document", "search.result.other": "# matching documents", "search.result.placeholder": "Type to start searching", "search.result.term.missing": "Missing", "select.version": "Select version"}}</script>
    
    
      <script src="../../../assets/javascripts/bundle.f1b6f286.min.js"></script>
      
        <script src="/flarelytics/client.js"></script>
      
        <script src="https://cdn.jsdelivr.net/npm/algoliasearch@5.20.0/dist/lite/builds/browser.umd.js"></script>
      
        <script src="https://cdn.jsdelivr.net/npm/instantsearch.js@4.77.3/dist/instantsearch.production.min.js"></script>
      
        <script src="/javascripts/algolia-search.js"></script>
      
    
  <script id="init-glightbox">const lightbox = GLightbox({"touchNavigation": true, "loop": false, "zoomable": true, "draggable": true, "openEffect": "zoom", "closeEffect": "zoom", "slideEffect": "slide"});
document$.subscribe(() => { lightbox.reload() });
</script>
</body></html>