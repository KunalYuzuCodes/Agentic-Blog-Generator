<!DOCTYPE html><html lang="en" class="js-focus-visible js" data-js-focus-visible=""><head>
    
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width,initial-scale=1">
      
        <meta name="description" content="Agent Framework / shim to use Pydantic with LLMs">
      
      
      
        <link rel="canonical" href="https://ai.pydantic.dev/api/pydantic_evals/evaluators/">
      
      
        <link rel="prev" href="../dataset/">
      
      
        <link rel="next" href="../reporting/">
      
      
      <link rel="icon" href="../../../favicon.ico">
      <meta name="generator" content="mkdocs-1.6.1, mkdocs-material-9.6.5">
    
    
      
        <title>pydantic_evals.evaluators - PydanticAI</title>
      
    
    
      <link rel="stylesheet" href="../../../assets/stylesheets/main.8608ea7d.min.css">
      
        
        <link rel="stylesheet" href="../../../assets/stylesheets/palette.06af60db.min.css">
      
      


    
    
      
    
    
      
        
        
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,300i,400,400i,700,700i%7CRoboto+Mono:400,400i,700,700i&amp;display=fallback">
        <style>:root{--md-text-font:"Roboto";--md-code-font:"Roboto Mono"}</style>
      
    
    
      <link rel="stylesheet" href="../../../assets/_mkdocstrings.css">
    
      <link rel="stylesheet" href="../../../extra/tweaks.css">
    
    <script>__md_scope=new URL("../../..",location),__md_hash=e=>[...e].reduce(((e,_)=>(e<<5)-e+_.charCodeAt(0)),0),__md_get=(e,_=localStorage,t=__md_scope)=>JSON.parse(_.getItem(t.pathname+"."+e)),__md_set=(e,_,t=localStorage,a=__md_scope)=>{try{t.setItem(a.pathname+"."+e,JSON.stringify(_))}catch(e){}}</script>
    
      

    
    
      
        <meta property="og:type" content="website">
      
        <meta property="og:title" content="pydantic_evals.evaluators - PydanticAI">
      
        <meta property="og:description" content="Agent Framework / shim to use Pydantic with LLMs">
      
        <meta property="og:image" content="https://ai.pydantic.dev/assets/images/social/api/pydantic_evals/evaluators.png">
      
        <meta property="og:image:type" content="image/png">
      
        <meta property="og:image:width" content="1200">
      
        <meta property="og:image:height" content="630">
      
        <meta property="og:url" content="https://ai.pydantic.dev/api/pydantic_evals/evaluators/">
      
        <meta name="twitter:card" content="summary_large_image">
      
        <meta name="twitter:title" content="pydantic_evals.evaluators - PydanticAI">
      
        <meta name="twitter:description" content="Agent Framework / shim to use Pydantic with LLMs">
      
        <meta name="twitter:image" content="https://ai.pydantic.dev/assets/images/social/api/pydantic_evals/evaluators.png">
      
    
    
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
      
        
        <a href="#pydantic_evalsevaluators" class="md-skip">
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
            
              pydantic_evals.evaluators
            
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
      <a href="../../pydantic_graph/graph/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../pydantic_graph/nodes/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.nodes
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../pydantic_graph/persistence/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.persistence
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../pydantic_graph/mermaid/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.mermaid
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../pydantic_graph/exceptions/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.exceptions
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../dataset/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.dataset
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
    
  
  
  
    <li class="md-nav__item md-nav__item--active">
      
      <input class="md-nav__toggle md-toggle" type="checkbox" id="__toc">
      
      
        
      
      
        <label class="md-nav__link md-nav__link--active" for="__toc">
          
  
  <span class="md-ellipsis">
    pydantic_evals.evaluators
    
  </span>
  

          <span class="md-nav__icon md-icon"></span>
        </label>
      
      <a href="./" class="md-nav__link md-nav__link--active">
        
  
  <span class="md-ellipsis">
    pydantic_evals.evaluators
    
  </span>
  

      </a>
      
        

<nav class="md-nav md-nav--secondary" aria-label="Table of contents">
  
  
  
    
  
  
    <label class="md-nav__title" for="__toc">
      <span class="md-nav__icon md-icon"></span>
      Table of contents
    </label>
    <ul class="md-nav__list" data-md-component="toc">
      
        <li class="md-nav__item">
  <a href="#pydantic_evals.evaluators" class="md-nav__link">
    <span class="md-ellipsis">
      evaluators
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_evals.evaluators.Contains" class="md-nav__link">
    <span class="md-ellipsis">
      Contains
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_evals.evaluators.Equals" class="md-nav__link">
    <span class="md-ellipsis">
      Equals
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_evals.evaluators.EqualsExpected" class="md-nav__link">
    <span class="md-ellipsis">
      EqualsExpected
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_evals.evaluators.HasMatchingSpan" class="md-nav__link">
    <span class="md-ellipsis">
      HasMatchingSpan
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_evals.evaluators.IsInstance" class="md-nav__link">
    <span class="md-ellipsis">
      IsInstance
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_evals.evaluators.LLMJudge" class="md-nav__link">
    <span class="md-ellipsis">
      LLMJudge
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_evals.evaluators.MaxDuration" class="md-nav__link">
    <span class="md-ellipsis">
      MaxDuration
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_evals.evaluators.Python" class="md-nav__link">
    <span class="md-ellipsis">
      Python
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_evals.evaluators.EvaluatorContext" class="md-nav__link">
    <span class="md-ellipsis">
      EvaluatorContext
    </span>
  </a>
  
    <nav class="md-nav" aria-label="EvaluatorContext">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.evaluators.EvaluatorContext.name" class="md-nav__link">
    <span class="md-ellipsis">
      name
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.evaluators.EvaluatorContext.inputs" class="md-nav__link">
    <span class="md-ellipsis">
      inputs
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.evaluators.EvaluatorContext.metadata" class="md-nav__link">
    <span class="md-ellipsis">
      metadata
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.evaluators.EvaluatorContext.expected_output" class="md-nav__link">
    <span class="md-ellipsis">
      expected_output
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.evaluators.EvaluatorContext.output" class="md-nav__link">
    <span class="md-ellipsis">
      output
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.evaluators.EvaluatorContext.duration" class="md-nav__link">
    <span class="md-ellipsis">
      duration
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.evaluators.EvaluatorContext.attributes" class="md-nav__link">
    <span class="md-ellipsis">
      attributes
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.evaluators.EvaluatorContext.metrics" class="md-nav__link">
    <span class="md-ellipsis">
      metrics
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.evaluators.EvaluatorContext.span_tree" class="md-nav__link">
    <span class="md-ellipsis">
      span_tree
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_evals.evaluators.EvaluationReason" class="md-nav__link">
    <span class="md-ellipsis">
      EvaluationReason
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_evals.evaluators.EvaluationResult" class="md-nav__link">
    <span class="md-ellipsis">
      EvaluationResult
    </span>
  </a>
  
    <nav class="md-nav" aria-label="EvaluationResult">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.evaluators.EvaluationResult.downcast" class="md-nav__link">
    <span class="md-ellipsis">
      downcast
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_evals.evaluators.Evaluator" class="md-nav__link">
    <span class="md-ellipsis">
      Evaluator
    </span>
  </a>
  
    <nav class="md-nav" aria-label="Evaluator">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.evaluators.Evaluator.name" class="md-nav__link">
    <span class="md-ellipsis">
      name
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.evaluators.Evaluator.evaluate" class="md-nav__link">
    <span class="md-ellipsis">
      evaluate
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.evaluators.Evaluator.evaluate_sync" class="md-nav__link">
    <span class="md-ellipsis">
      evaluate_sync
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.evaluators.Evaluator.evaluate_async" class="md-nav__link">
    <span class="md-ellipsis">
      evaluate_async
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.evaluators.Evaluator.serialize" class="md-nav__link">
    <span class="md-ellipsis">
      serialize
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_evals.evaluators.EvaluatorOutput" class="md-nav__link">
    <span class="md-ellipsis">
      EvaluatorOutput
    </span>
  </a>
  
</li>
      
    </ul>
  
</nav>
      
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../reporting/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.reporting
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../otel/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.otel
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../generation/" class="md-nav__link">
        
  
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
  <a href="#pydantic_evals.evaluators" class="md-nav__link">
    <span class="md-ellipsis">
      evaluators
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_evals.evaluators.Contains" class="md-nav__link">
    <span class="md-ellipsis">
      Contains
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_evals.evaluators.Equals" class="md-nav__link">
    <span class="md-ellipsis">
      Equals
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_evals.evaluators.EqualsExpected" class="md-nav__link">
    <span class="md-ellipsis">
      EqualsExpected
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_evals.evaluators.HasMatchingSpan" class="md-nav__link">
    <span class="md-ellipsis">
      HasMatchingSpan
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_evals.evaluators.IsInstance" class="md-nav__link">
    <span class="md-ellipsis">
      IsInstance
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_evals.evaluators.LLMJudge" class="md-nav__link">
    <span class="md-ellipsis">
      LLMJudge
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_evals.evaluators.MaxDuration" class="md-nav__link">
    <span class="md-ellipsis">
      MaxDuration
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_evals.evaluators.Python" class="md-nav__link">
    <span class="md-ellipsis">
      Python
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_evals.evaluators.EvaluatorContext" class="md-nav__link">
    <span class="md-ellipsis">
      EvaluatorContext
    </span>
  </a>
  
    <nav class="md-nav" aria-label="EvaluatorContext">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.evaluators.EvaluatorContext.name" class="md-nav__link">
    <span class="md-ellipsis">
      name
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.evaluators.EvaluatorContext.inputs" class="md-nav__link">
    <span class="md-ellipsis">
      inputs
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.evaluators.EvaluatorContext.metadata" class="md-nav__link">
    <span class="md-ellipsis">
      metadata
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.evaluators.EvaluatorContext.expected_output" class="md-nav__link">
    <span class="md-ellipsis">
      expected_output
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.evaluators.EvaluatorContext.output" class="md-nav__link">
    <span class="md-ellipsis">
      output
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.evaluators.EvaluatorContext.duration" class="md-nav__link">
    <span class="md-ellipsis">
      duration
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.evaluators.EvaluatorContext.attributes" class="md-nav__link">
    <span class="md-ellipsis">
      attributes
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.evaluators.EvaluatorContext.metrics" class="md-nav__link">
    <span class="md-ellipsis">
      metrics
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.evaluators.EvaluatorContext.span_tree" class="md-nav__link">
    <span class="md-ellipsis">
      span_tree
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_evals.evaluators.EvaluationReason" class="md-nav__link">
    <span class="md-ellipsis">
      EvaluationReason
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_evals.evaluators.EvaluationResult" class="md-nav__link">
    <span class="md-ellipsis">
      EvaluationResult
    </span>
  </a>
  
    <nav class="md-nav" aria-label="EvaluationResult">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.evaluators.EvaluationResult.downcast" class="md-nav__link">
    <span class="md-ellipsis">
      downcast
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_evals.evaluators.Evaluator" class="md-nav__link">
    <span class="md-ellipsis">
      Evaluator
    </span>
  </a>
  
    <nav class="md-nav" aria-label="Evaluator">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.evaluators.Evaluator.name" class="md-nav__link">
    <span class="md-ellipsis">
      name
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.evaluators.Evaluator.evaluate" class="md-nav__link">
    <span class="md-ellipsis">
      evaluate
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.evaluators.Evaluator.evaluate_sync" class="md-nav__link">
    <span class="md-ellipsis">
      evaluate_sync
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.evaluators.Evaluator.evaluate_async" class="md-nav__link">
    <span class="md-ellipsis">
      evaluate_async
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_evals.evaluators.Evaluator.serialize" class="md-nav__link">
    <span class="md-ellipsis">
      serialize
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_evals.evaluators.EvaluatorOutput" class="md-nav__link">
    <span class="md-ellipsis">
      EvaluatorOutput
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
                
                  


  
  


<h1 id="pydantic_evalsevaluators"><code>pydantic_evals.evaluators</code></h1>


<div class="doc doc-object doc-module">



<a id="pydantic_evals.evaluators"></a>
    <div class="doc doc-contents first">








  <div class="doc doc-children">































<div class="doc doc-object doc-class">



<h3 id="pydantic_evals.evaluators.Contains" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">Contains</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span>

</h3>


    <div class="doc doc-contents ">
            <p class="doc doc-class-bases">
              Bases: <code><a class="autorefs autorefs-internal" title="pydantic_evals.evaluators.evaluator.Evaluator" href="#pydantic_evals.evaluators.Evaluator">Evaluator</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#object">object</a>, <a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#object">object</a>, <a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#object">object</a>]</code></p>


        <p>Check if the output contains the expected output.</p>
<p>For strings, checks if expected_output is a substring of output.
For lists/tuples, checks if expected_output is in output.
For dicts, checks if all key-value pairs in expected_output are in output.</p>
<p>Note: case_sensitive only applies when both the value and output are strings.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_evals/pydantic_evals/evaluators/common.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 56</span>
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
<span class="normal">114</span>
<span class="normal">115</span>
<span class="normal">116</span>
<span class="normal">117</span>
<span class="normal">118</span>
<span class="normal">119</span>
<span class="normal">120</span>
<span class="normal">121</span></pre></div></td><td class="code"><div><pre id="__code_0"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_0 > code"></button><code tabindex="0"><span class="nd">@dataclass</span>
<span class="k">class</span><span class="w"> </span><span class="nc">Contains</span><span class="p">(</span><span class="n">Evaluator</span><span class="p">[</span><span class="nb">object</span><span class="p">,</span> <span class="nb">object</span><span class="p">,</span> <span class="nb">object</span><span class="p">]):</span>
<span class="w">    </span><span class="sd">"""Check if the output contains the expected output.</span>

<span class="sd">    For strings, checks if expected_output is a substring of output.</span>
<span class="sd">    For lists/tuples, checks if expected_output is in output.</span>
<span class="sd">    For dicts, checks if all key-value pairs in expected_output are in output.</span>

<span class="sd">    Note: case_sensitive only applies when both the value and output are strings.</span>
<span class="sd">    """</span>

    <span class="n">value</span><span class="p">:</span> <span class="n">Any</span>
    <span class="n">case_sensitive</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>
    <span class="n">as_strings</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">evaluate</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">ctx</span><span class="p">:</span> <span class="n">EvaluatorContext</span><span class="p">[</span><span class="nb">object</span><span class="p">,</span> <span class="nb">object</span><span class="p">,</span> <span class="nb">object</span><span class="p">],</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">EvaluationReason</span><span class="p">:</span>
        <span class="c1"># Convert objects to strings if requested</span>
        <span class="n">failure_reason</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="n">as_strings</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">as_strings</span> <span class="ow">or</span> <span class="p">(</span><span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">value</span><span class="p">,</span> <span class="nb">str</span><span class="p">)</span> <span class="ow">and</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">ctx</span><span class="o">.</span><span class="n">output</span><span class="p">,</span> <span class="nb">str</span><span class="p">))</span>
        <span class="k">if</span> <span class="n">as_strings</span><span class="p">:</span>
            <span class="n">output_str</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">ctx</span><span class="o">.</span><span class="n">output</span><span class="p">)</span>
            <span class="n">expected_str</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>

            <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">case_sensitive</span><span class="p">:</span>
                <span class="n">output_str</span> <span class="o">=</span> <span class="n">output_str</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span>
                <span class="n">expected_str</span> <span class="o">=</span> <span class="n">expected_str</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span>

            <span class="n">failure_reason</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
            <span class="k">if</span> <span class="n">expected_str</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">output_str</span><span class="p">:</span>
                <span class="n">output_trunc</span> <span class="o">=</span> <span class="n">_truncated_repr</span><span class="p">(</span><span class="n">output_str</span><span class="p">,</span> <span class="n">max_length</span><span class="o">=</span><span class="mi">100</span><span class="p">)</span>
                <span class="n">expected_trunc</span> <span class="o">=</span> <span class="n">_truncated_repr</span><span class="p">(</span><span class="n">expected_str</span><span class="p">,</span> <span class="n">max_length</span><span class="o">=</span><span class="mi">100</span><span class="p">)</span>
                <span class="n">failure_reason</span> <span class="o">=</span> <span class="sa">f</span><span class="s1">'Output string </span><span class="si">{</span><span class="n">output_trunc</span><span class="si">}</span><span class="s1"> does not contain expected string </span><span class="si">{</span><span class="n">expected_trunc</span><span class="si">}</span><span class="s1">'</span>
            <span class="k">return</span> <span class="n">EvaluationReason</span><span class="p">(</span><span class="n">value</span><span class="o">=</span><span class="n">failure_reason</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">,</span> <span class="n">reason</span><span class="o">=</span><span class="n">failure_reason</span><span class="p">)</span>

        <span class="k">try</span><span class="p">:</span>
            <span class="c1"># Handle different collection types</span>
            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">ctx</span><span class="o">.</span><span class="n">output</span><span class="p">,</span> <span class="nb">dict</span><span class="p">):</span>
                <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">value</span><span class="p">,</span> <span class="nb">dict</span><span class="p">):</span>
                    <span class="c1"># Cast to Any to avoid type checking issues</span>
                    <span class="n">output_dict</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="nb">dict</span><span class="p">[</span><span class="n">Any</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span> <span class="n">ctx</span><span class="o">.</span><span class="n">output</span><span class="p">)</span>  <span class="c1"># pyright: ignore[reportUnknownMemberType]</span>
                    <span class="n">expected_dict</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="nb">dict</span><span class="p">[</span><span class="n">Any</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>  <span class="c1"># pyright: ignore[reportUnknownMemberType]</span>
                    <span class="k">for</span> <span class="n">k</span> <span class="ow">in</span> <span class="n">expected_dict</span><span class="p">:</span>
                        <span class="k">if</span> <span class="n">k</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">output_dict</span><span class="p">:</span>
                            <span class="n">k_trunc</span> <span class="o">=</span> <span class="n">_truncated_repr</span><span class="p">(</span><span class="n">k</span><span class="p">,</span> <span class="n">max_length</span><span class="o">=</span><span class="mi">30</span><span class="p">)</span>
                            <span class="n">failure_reason</span> <span class="o">=</span> <span class="sa">f</span><span class="s1">'Output dictionary does not contain expected key </span><span class="si">{</span><span class="n">k_trunc</span><span class="si">}</span><span class="s1">'</span>
                            <span class="k">break</span>
                        <span class="k">elif</span> <span class="n">output_dict</span><span class="p">[</span><span class="n">k</span><span class="p">]</span> <span class="o">!=</span> <span class="n">expected_dict</span><span class="p">[</span><span class="n">k</span><span class="p">]:</span>
                            <span class="n">k_trunc</span> <span class="o">=</span> <span class="n">_truncated_repr</span><span class="p">(</span><span class="n">k</span><span class="p">,</span> <span class="n">max_length</span><span class="o">=</span><span class="mi">30</span><span class="p">)</span>
                            <span class="n">output_v_trunc</span> <span class="o">=</span> <span class="n">_truncated_repr</span><span class="p">(</span><span class="n">output_dict</span><span class="p">[</span><span class="n">k</span><span class="p">],</span> <span class="n">max_length</span><span class="o">=</span><span class="mi">100</span><span class="p">)</span>
                            <span class="n">expected_v_trunc</span> <span class="o">=</span> <span class="n">_truncated_repr</span><span class="p">(</span><span class="n">expected_dict</span><span class="p">[</span><span class="n">k</span><span class="p">],</span> <span class="n">max_length</span><span class="o">=</span><span class="mi">100</span><span class="p">)</span>
                            <span class="n">failure_reason</span> <span class="o">=</span> <span class="sa">f</span><span class="s1">'Output dictionary has different value for key </span><span class="si">{</span><span class="n">k_trunc</span><span class="si">}</span><span class="s1">: </span><span class="si">{</span><span class="n">output_v_trunc</span><span class="si">}</span><span class="s1"> != </span><span class="si">{</span><span class="n">expected_v_trunc</span><span class="si">}</span><span class="s1">'</span>
                            <span class="k">break</span>
                <span class="k">else</span><span class="p">:</span>
                    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">ctx</span><span class="o">.</span><span class="n">output</span><span class="p">:</span>  <span class="c1"># pyright: ignore[reportUnknownMemberType]</span>
                        <span class="n">output_trunc</span> <span class="o">=</span> <span class="n">_truncated_repr</span><span class="p">(</span><span class="n">ctx</span><span class="o">.</span><span class="n">output</span><span class="p">,</span> <span class="n">max_length</span><span class="o">=</span><span class="mi">200</span><span class="p">)</span>  <span class="c1"># pyright: ignore[reportUnknownMemberType]</span>
                        <span class="n">failure_reason</span> <span class="o">=</span> <span class="sa">f</span><span class="s1">'Output </span><span class="si">{</span><span class="n">output_trunc</span><span class="si">}</span><span class="s1"> does not contain provided value as a key'</span>
            <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">ctx</span><span class="o">.</span><span class="n">output</span><span class="p">:</span>  <span class="c1"># pyright: ignore[reportOperatorIssue]  # will be handled by except block</span>
                <span class="n">output_trunc</span> <span class="o">=</span> <span class="n">_truncated_repr</span><span class="p">(</span><span class="n">ctx</span><span class="o">.</span><span class="n">output</span><span class="p">,</span> <span class="n">max_length</span><span class="o">=</span><span class="mi">200</span><span class="p">)</span>
                <span class="n">failure_reason</span> <span class="o">=</span> <span class="sa">f</span><span class="s1">'Output </span><span class="si">{</span><span class="n">output_trunc</span><span class="si">}</span><span class="s1"> does not contain provided value'</span>
        <span class="k">except</span> <span class="p">(</span><span class="ne">TypeError</span><span class="p">,</span> <span class="ne">ValueError</span><span class="p">)</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="n">failure_reason</span> <span class="o">=</span> <span class="sa">f</span><span class="s1">'Containment check failed: </span><span class="si">{</span><span class="n">e</span><span class="si">}</span><span class="s1">'</span>

        <span class="k">return</span> <span class="n">EvaluationReason</span><span class="p">(</span><span class="n">value</span><span class="o">=</span><span class="n">failure_reason</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">,</span> <span class="n">reason</span><span class="o">=</span><span class="n">failure_reason</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">





  </div>

    </div>

</div>






<div class="doc doc-object doc-class">



<h3 id="pydantic_evals.evaluators.Equals" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">Equals</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span>

</h3>


    <div class="doc doc-contents ">
            <p class="doc doc-class-bases">
              Bases: <code><a class="autorefs autorefs-internal" title="pydantic_evals.evaluators.evaluator.Evaluator" href="#pydantic_evals.evaluators.Evaluator">Evaluator</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#object">object</a>, <a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#object">object</a>, <a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#object">object</a>]</code></p>


        <p>Check if the output exactly equals the provided value.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_evals/pydantic_evals/evaluators/common.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">25</span>
<span class="normal">26</span>
<span class="normal">27</span>
<span class="normal">28</span>
<span class="normal">29</span>
<span class="normal">30</span>
<span class="normal">31</span>
<span class="normal">32</span></pre></div></td><td class="code"><div><pre id="__code_1"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_1 > code"></button><code><span class="nd">@dataclass</span>
<span class="k">class</span><span class="w"> </span><span class="nc">Equals</span><span class="p">(</span><span class="n">Evaluator</span><span class="p">[</span><span class="nb">object</span><span class="p">,</span> <span class="nb">object</span><span class="p">,</span> <span class="nb">object</span><span class="p">]):</span>
<span class="w">    </span><span class="sd">"""Check if the output exactly equals the provided value."""</span>

    <span class="n">value</span><span class="p">:</span> <span class="n">Any</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">evaluate</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ctx</span><span class="p">:</span> <span class="n">EvaluatorContext</span><span class="p">[</span><span class="nb">object</span><span class="p">,</span> <span class="nb">object</span><span class="p">,</span> <span class="nb">object</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">ctx</span><span class="o">.</span><span class="n">output</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">





  </div>

    </div>

</div>






<div class="doc doc-object doc-class">



<h3 id="pydantic_evals.evaluators.EqualsExpected" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">EqualsExpected</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span>

</h3>


    <div class="doc doc-contents ">
            <p class="doc doc-class-bases">
              Bases: <code><a class="autorefs autorefs-internal" title="pydantic_evals.evaluators.evaluator.Evaluator" href="#pydantic_evals.evaluators.Evaluator">Evaluator</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#object">object</a>, <a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#object">object</a>, <a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#object">object</a>]</code></p>


        <p>Check if the output exactly equals the expected output.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_evals/pydantic_evals/evaluators/common.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">35</span>
<span class="normal">36</span>
<span class="normal">37</span>
<span class="normal">38</span>
<span class="normal">39</span>
<span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span></pre></div></td><td class="code"><div><pre id="__code_2"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_2 > code"></button><code><span class="nd">@dataclass</span>
<span class="k">class</span><span class="w"> </span><span class="nc">EqualsExpected</span><span class="p">(</span><span class="n">Evaluator</span><span class="p">[</span><span class="nb">object</span><span class="p">,</span> <span class="nb">object</span><span class="p">,</span> <span class="nb">object</span><span class="p">]):</span>
<span class="w">    </span><span class="sd">"""Check if the output exactly equals the expected output."""</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">evaluate</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ctx</span><span class="p">:</span> <span class="n">EvaluatorContext</span><span class="p">[</span><span class="nb">object</span><span class="p">,</span> <span class="nb">object</span><span class="p">,</span> <span class="nb">object</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="nb">bool</span> <span class="o">|</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">bool</span><span class="p">]:</span>
        <span class="k">if</span> <span class="n">ctx</span><span class="o">.</span><span class="n">expected_output</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">return</span> <span class="p">{}</span>  <span class="c1"># Only compare if expected output is provided</span>
        <span class="k">return</span> <span class="n">ctx</span><span class="o">.</span><span class="n">output</span> <span class="o">==</span> <span class="n">ctx</span><span class="o">.</span><span class="n">expected_output</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">





  </div>

    </div>

</div>






<div class="doc doc-object doc-class">



<h3 id="pydantic_evals.evaluators.HasMatchingSpan" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">HasMatchingSpan</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span>

</h3>


    <div class="doc doc-contents ">
            <p class="doc doc-class-bases">
              Bases: <code><a class="autorefs autorefs-internal" title="pydantic_evals.evaluators.evaluator.Evaluator" href="#pydantic_evals.evaluators.Evaluator">Evaluator</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#object">object</a>, <a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#object">object</a>, <a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#object">object</a>]</code></p>


        <p>Check if the span tree contains a span that matches the specified query.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_evals/pydantic_evals/evaluators/common.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">179</span>
<span class="normal">180</span>
<span class="normal">181</span>
<span class="normal">182</span>
<span class="normal">183</span>
<span class="normal">184</span>
<span class="normal">185</span>
<span class="normal">186</span>
<span class="normal">187</span>
<span class="normal">188</span>
<span class="normal">189</span></pre></div></td><td class="code"><div><pre id="__code_3"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_3 > code"></button><code><span class="nd">@dataclass</span>
<span class="k">class</span><span class="w"> </span><span class="nc">HasMatchingSpan</span><span class="p">(</span><span class="n">Evaluator</span><span class="p">[</span><span class="nb">object</span><span class="p">,</span> <span class="nb">object</span><span class="p">,</span> <span class="nb">object</span><span class="p">]):</span>
<span class="w">    </span><span class="sd">"""Check if the span tree contains a span that matches the specified query."""</span>

    <span class="n">query</span><span class="p">:</span> <span class="n">SpanQuery</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">evaluate</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">ctx</span><span class="p">:</span> <span class="n">EvaluatorContext</span><span class="p">[</span><span class="nb">object</span><span class="p">,</span> <span class="nb">object</span><span class="p">,</span> <span class="nb">object</span><span class="p">],</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">ctx</span><span class="o">.</span><span class="n">span_tree</span><span class="o">.</span><span class="n">any</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">query</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">





  </div>

    </div>

</div>






<div class="doc doc-object doc-class">



<h3 id="pydantic_evals.evaluators.IsInstance" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">IsInstance</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span>

</h3>


    <div class="doc doc-contents ">
            <p class="doc doc-class-bases">
              Bases: <code><a class="autorefs autorefs-internal" title="pydantic_evals.evaluators.evaluator.Evaluator" href="#pydantic_evals.evaluators.Evaluator">Evaluator</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#object">object</a>, <a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#object">object</a>, <a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#object">object</a>]</code></p>


        <p>Check if the output is an instance of a type with the given name.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_evals/pydantic_evals/evaluators/common.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">124</span>
<span class="normal">125</span>
<span class="normal">126</span>
<span class="normal">127</span>
<span class="normal">128</span>
<span class="normal">129</span>
<span class="normal">130</span>
<span class="normal">131</span>
<span class="normal">132</span>
<span class="normal">133</span>
<span class="normal">134</span>
<span class="normal">135</span>
<span class="normal">136</span>
<span class="normal">137</span>
<span class="normal">138</span>
<span class="normal">139</span></pre></div></td><td class="code"><div><pre id="__code_4"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_4 > code"></button><code><span class="nd">@dataclass</span>
<span class="k">class</span><span class="w"> </span><span class="nc">IsInstance</span><span class="p">(</span><span class="n">Evaluator</span><span class="p">[</span><span class="nb">object</span><span class="p">,</span> <span class="nb">object</span><span class="p">,</span> <span class="nb">object</span><span class="p">]):</span>
<span class="w">    </span><span class="sd">"""Check if the output is an instance of a type with the given name."""</span>

    <span class="n">type_name</span><span class="p">:</span> <span class="nb">str</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">evaluate</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ctx</span><span class="p">:</span> <span class="n">EvaluatorContext</span><span class="p">[</span><span class="nb">object</span><span class="p">,</span> <span class="nb">object</span><span class="p">,</span> <span class="nb">object</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">EvaluationReason</span><span class="p">:</span>
        <span class="n">output</span> <span class="o">=</span> <span class="n">ctx</span><span class="o">.</span><span class="n">output</span>
        <span class="k">for</span> <span class="bp">cls</span> <span class="ow">in</span> <span class="nb">type</span><span class="p">(</span><span class="n">output</span><span class="p">)</span><span class="o">.</span><span class="vm">__mro__</span><span class="p">:</span>
            <span class="k">if</span> <span class="bp">cls</span><span class="o">.</span><span class="vm">__name__</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">type_name</span> <span class="ow">or</span> <span class="bp">cls</span><span class="o">.</span><span class="vm">__qualname__</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">type_name</span><span class="p">:</span>
                <span class="k">return</span> <span class="n">EvaluationReason</span><span class="p">(</span><span class="n">value</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>

        <span class="n">reason</span> <span class="o">=</span> <span class="sa">f</span><span class="s1">'output is of type </span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="n">output</span><span class="p">)</span><span class="o">.</span><span class="vm">__name__</span><span class="si">}</span><span class="s1">'</span>
        <span class="k">if</span> <span class="nb">type</span><span class="p">(</span><span class="n">output</span><span class="p">)</span><span class="o">.</span><span class="vm">__qualname__</span> <span class="o">!=</span> <span class="nb">type</span><span class="p">(</span><span class="n">output</span><span class="p">)</span><span class="o">.</span><span class="vm">__name__</span><span class="p">:</span>
            <span class="n">reason</span> <span class="o">+=</span> <span class="sa">f</span><span class="s1">' (qualname: </span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="n">output</span><span class="p">)</span><span class="o">.</span><span class="vm">__qualname__</span><span class="si">}</span><span class="s1">)'</span>
        <span class="k">return</span> <span class="n">EvaluationReason</span><span class="p">(</span><span class="n">value</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">reason</span><span class="o">=</span><span class="n">reason</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">





  </div>

    </div>

</div>






<div class="doc doc-object doc-class">



<h3 id="pydantic_evals.evaluators.LLMJudge" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">LLMJudge</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span>

</h3>


    <div class="doc doc-contents ">
            <p class="doc doc-class-bases">
              Bases: <code><a class="autorefs autorefs-internal" title="pydantic_evals.evaluators.evaluator.Evaluator" href="#pydantic_evals.evaluators.Evaluator">Evaluator</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#object">object</a>, <a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#object">object</a>, <a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#object">object</a>]</code></p>


        <p>Judge whether the output of a language model meets the criteria of a provided rubric.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_evals/pydantic_evals/evaluators/common.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">156</span>
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
<span class="normal">176</span></pre></div></td><td class="code"><div><pre id="__code_5"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_5 > code"></button><code><span class="nd">@dataclass</span>
<span class="k">class</span><span class="w"> </span><span class="nc">LLMJudge</span><span class="p">(</span><span class="n">Evaluator</span><span class="p">[</span><span class="nb">object</span><span class="p">,</span> <span class="nb">object</span><span class="p">,</span> <span class="nb">object</span><span class="p">]):</span>
<span class="w">    </span><span class="sd">"""Judge whether the output of a language model meets the criteria of a provided rubric."""</span>

    <span class="n">rubric</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">model</span><span class="p">:</span> <span class="n">models</span><span class="o">.</span><span class="n">Model</span> <span class="o">|</span> <span class="n">models</span><span class="o">.</span><span class="n">KnownModelName</span> <span class="o">=</span> <span class="s1">'openai:gpt-4o'</span>
    <span class="n">include_input</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>

    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">evaluate</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">ctx</span><span class="p">:</span> <span class="n">EvaluatorContext</span><span class="p">[</span><span class="nb">object</span><span class="p">,</span> <span class="nb">object</span><span class="p">,</span> <span class="nb">object</span><span class="p">],</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">EvaluationReason</span><span class="p">:</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">include_input</span><span class="p">:</span>
            <span class="kn">from</span><span class="w"> </span><span class="nn">.llm_as_a_judge</span><span class="w"> </span><span class="kn">import</span> <span class="n">judge_input_output</span>

            <span class="n">grading_output</span> <span class="o">=</span> <span class="k">await</span> <span class="n">judge_input_output</span><span class="p">(</span><span class="n">ctx</span><span class="o">.</span><span class="n">inputs</span><span class="p">,</span> <span class="n">ctx</span><span class="o">.</span><span class="n">output</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">rubric</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">model</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="kn">from</span><span class="w"> </span><span class="nn">.llm_as_a_judge</span><span class="w"> </span><span class="kn">import</span> <span class="n">judge_output</span>

            <span class="n">grading_output</span> <span class="o">=</span> <span class="k">await</span> <span class="n">judge_output</span><span class="p">(</span><span class="n">ctx</span><span class="o">.</span><span class="n">output</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">rubric</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">model</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">EvaluationReason</span><span class="p">(</span><span class="n">value</span><span class="o">=</span><span class="n">grading_output</span><span class="o">.</span><span class="n">pass_</span><span class="p">,</span> <span class="n">reason</span><span class="o">=</span><span class="n">grading_output</span><span class="o">.</span><span class="n">reason</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">





  </div>

    </div>

</div>






<div class="doc doc-object doc-class">



<h3 id="pydantic_evals.evaluators.MaxDuration" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">MaxDuration</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span>

</h3>


    <div class="doc doc-contents ">
            <p class="doc doc-class-bases">
              Bases: <code><a class="autorefs autorefs-internal" title="pydantic_evals.evaluators.evaluator.Evaluator" href="#pydantic_evals.evaluators.Evaluator">Evaluator</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#object">object</a>, <a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#object">object</a>, <a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#object">object</a>]</code></p>


        <p>Check if the execution time is under the specified maximum.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_evals/pydantic_evals/evaluators/common.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">142</span>
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
<span class="normal">153</span></pre></div></td><td class="code"><div><pre id="__code_6"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_6 > code"></button><code><span class="nd">@dataclass</span>
<span class="k">class</span><span class="w"> </span><span class="nc">MaxDuration</span><span class="p">(</span><span class="n">Evaluator</span><span class="p">[</span><span class="nb">object</span><span class="p">,</span> <span class="nb">object</span><span class="p">,</span> <span class="nb">object</span><span class="p">]):</span>
<span class="w">    </span><span class="sd">"""Check if the execution time is under the specified maximum."""</span>

    <span class="n">seconds</span><span class="p">:</span> <span class="nb">float</span> <span class="o">|</span> <span class="n">timedelta</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">evaluate</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ctx</span><span class="p">:</span> <span class="n">EvaluatorContext</span><span class="p">[</span><span class="nb">object</span><span class="p">,</span> <span class="nb">object</span><span class="p">,</span> <span class="nb">object</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
        <span class="n">duration</span> <span class="o">=</span> <span class="n">timedelta</span><span class="p">(</span><span class="n">seconds</span><span class="o">=</span><span class="n">ctx</span><span class="o">.</span><span class="n">duration</span><span class="p">)</span>
        <span class="n">seconds</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">seconds</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">seconds</span><span class="p">,</span> <span class="n">timedelta</span><span class="p">):</span>
            <span class="n">seconds</span> <span class="o">=</span> <span class="n">timedelta</span><span class="p">(</span><span class="n">seconds</span><span class="o">=</span><span class="n">seconds</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">duration</span> <span class="o">&lt;=</span> <span class="n">seconds</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">





  </div>

    </div>

</div>






<div class="doc doc-object doc-class">



<h3 id="pydantic_evals.evaluators.Python" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">Python</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span>

</h3>


    <div class="doc doc-contents ">
            <p class="doc doc-class-bases">
              Bases: <code><a class="autorefs autorefs-internal" title="pydantic_evals.evaluators.evaluator.Evaluator" href="#pydantic_evals.evaluators.Evaluator">Evaluator</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#object">object</a>, <a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#object">object</a>, <a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#object">object</a>]</code></p>


        <p>The output of this evaluator is the result of evaluating the provided Python expression.</p>
<p><strong><em>WARNING</em></strong>: this evaluator runs arbitrary Python code, so you should <strong><em>NEVER</em></strong> use it with untrusted inputs.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_evals/pydantic_evals/evaluators/common.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">193</span>
<span class="normal">194</span>
<span class="normal">195</span>
<span class="normal">196</span>
<span class="normal">197</span>
<span class="normal">198</span>
<span class="normal">199</span>
<span class="normal">200</span>
<span class="normal">201</span>
<span class="normal">202</span>
<span class="normal">203</span>
<span class="normal">204</span></pre></div></td><td class="code"><div><pre id="__code_7"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_7 > code"></button><code tabindex="0"><span class="nd">@dataclass</span>
<span class="k">class</span><span class="w"> </span><span class="nc">Python</span><span class="p">(</span><span class="n">Evaluator</span><span class="p">[</span><span class="nb">object</span><span class="p">,</span> <span class="nb">object</span><span class="p">,</span> <span class="nb">object</span><span class="p">]):</span>
<span class="w">    </span><span class="sd">"""The output of this evaluator is the result of evaluating the provided Python expression.</span>

<span class="sd">    ***WARNING***: this evaluator runs arbitrary Python code, so you should ***NEVER*** use it with untrusted inputs.</span>
<span class="sd">    """</span>

    <span class="n">expression</span><span class="p">:</span> <span class="nb">str</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">evaluate</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ctx</span><span class="p">:</span> <span class="n">EvaluatorContext</span><span class="p">[</span><span class="nb">object</span><span class="p">,</span> <span class="nb">object</span><span class="p">,</span> <span class="nb">object</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">EvaluatorOutput</span><span class="p">:</span>
        <span class="c1"># Evaluate the condition, exposing access to the evaluator context as `ctx`.</span>
        <span class="k">return</span> <span class="nb">eval</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">expression</span><span class="p">,</span> <span class="p">{</span><span class="s1">'ctx'</span><span class="p">:</span> <span class="n">ctx</span><span class="p">})</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">





  </div>

    </div>

</div>






<div class="doc doc-object doc-class">



<h3 id="pydantic_evals.evaluators.EvaluatorContext" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">EvaluatorContext</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span>

</h3>


    <div class="doc doc-contents ">
            <p class="doc doc-class-bases">
              Bases: <code><a class="autorefs autorefs-external" title="typing.Generic" href="https://docs.python.org/3/library/typing.html#typing.Generic">Generic</a>[<span title="pydantic_evals.evaluators.context.InputsT">InputsT</span>, <span title="pydantic_evals.evaluators.context.OutputT">OutputT</span>, <span title="pydantic_evals.evaluators.context.MetadataT">MetadataT</span>]</code></p>


        <p>Context for evaluating a task execution.</p>
<p>An instance of this class is the sole input to all Evaluators. It contains all the information
needed to evaluate the task execution, including inputs, outputs, metadata, and telemetry data.</p>
<p>Evaluators use this context to access the task inputs, actual output, expected output, and other
information when evaluating the result of the task execution.</p>
<p>Example:
</p><div class="language-python highlight"><pre id="__code_8"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_8 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">dataclasses</span><span class="w"> </span><span class="kn">import</span> <span class="n">dataclass</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_evals.evaluators</span><span class="w"> </span><span class="kn">import</span> <span class="n">Evaluator</span><span class="p">,</span> <span class="n">EvaluatorContext</span>


<span class="nd">@dataclass</span>
<span class="k">class</span><span class="w"> </span><span class="nc">ExactMatch</span><span class="p">(</span><span class="n">Evaluator</span><span class="p">):</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">evaluate</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ctx</span><span class="p">:</span> <span class="n">EvaluatorContext</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
        <span class="c1"># Use the context to access task inputs, outputs, and expected outputs</span>
        <span class="k">return</span> <span class="n">ctx</span><span class="o">.</span><span class="n">output</span> <span class="o">==</span> <span class="n">ctx</span><span class="o">.</span><span class="n">expected_output</span>
</code></pre></div><p></p>






              <details class="quote">
                <summary>Source code in <code>pydantic_evals/pydantic_evals/evaluators/context.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 30</span>
<span class="normal"> 31</span>
<span class="normal"> 32</span>
<span class="normal"> 33</span>
<span class="normal"> 34</span>
<span class="normal"> 35</span>
<span class="normal"> 36</span>
<span class="normal"> 37</span>
<span class="normal"> 38</span>
<span class="normal"> 39</span>
<span class="normal"> 40</span>
<span class="normal"> 41</span>
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
<span class="normal">102</span></pre></div></td><td class="code"><div><pre id="__code_9"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_9 > code"></button><code tabindex="0"><span class="nd">@dataclass</span>
<span class="k">class</span><span class="w"> </span><span class="nc">EvaluatorContext</span><span class="p">(</span><span class="n">Generic</span><span class="p">[</span><span class="n">InputsT</span><span class="p">,</span> <span class="n">OutputT</span><span class="p">,</span> <span class="n">MetadataT</span><span class="p">]):</span>
<span class="w">    </span><span class="sd">"""Context for evaluating a task execution.</span>

<span class="sd">    An instance of this class is the sole input to all Evaluators. It contains all the information</span>
<span class="sd">    needed to evaluate the task execution, including inputs, outputs, metadata, and telemetry data.</span>

<span class="sd">    Evaluators use this context to access the task inputs, actual output, expected output, and other</span>
<span class="sd">    information when evaluating the result of the task execution.</span>

<span class="sd">    Example:</span>
<span class="sd">    ```python</span>
<span class="sd">    from dataclasses import dataclass</span>

<span class="sd">    from pydantic_evals.evaluators import Evaluator, EvaluatorContext</span>


<span class="sd">    @dataclass</span>
<span class="sd">    class ExactMatch(Evaluator):</span>
<span class="sd">        def evaluate(self, ctx: EvaluatorContext) -&gt; bool:</span>
<span class="sd">            # Use the context to access task inputs, outputs, and expected outputs</span>
<span class="sd">            return ctx.output == ctx.expected_output</span>
<span class="sd">    ```</span>
<span class="sd">    """</span>

    <span class="n">name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span>
<span class="w">    </span><span class="sd">"""The name of the case."""</span>
    <span class="n">inputs</span><span class="p">:</span> <span class="n">InputsT</span>
<span class="w">    </span><span class="sd">"""The inputs provided to the task for this case."""</span>
    <span class="n">metadata</span><span class="p">:</span> <span class="n">MetadataT</span> <span class="o">|</span> <span class="kc">None</span>
<span class="w">    </span><span class="sd">"""Metadata associated with the case, if provided. May be None if no metadata was specified."""</span>
    <span class="n">expected_output</span><span class="p">:</span> <span class="n">OutputT</span> <span class="o">|</span> <span class="kc">None</span>
<span class="w">    </span><span class="sd">"""The expected output for the case, if provided. May be None if no expected output was specified."""</span>

    <span class="n">output</span><span class="p">:</span> <span class="n">OutputT</span>
<span class="w">    </span><span class="sd">"""The actual output produced by the task for this case."""</span>
    <span class="n">duration</span><span class="p">:</span> <span class="nb">float</span>
<span class="w">    </span><span class="sd">"""The duration of the task run for this case."""</span>
    <span class="n">_span_tree</span><span class="p">:</span> <span class="n">SpanTree</span> <span class="o">|</span> <span class="n">SpanTreeRecordingError</span> <span class="o">=</span> <span class="n">field</span><span class="p">(</span><span class="nb">repr</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
<span class="w">    </span><span class="sd">"""The span tree for the task run for this case.</span>

<span class="sd">    This will be `None` if `logfire.configure` has not been called.</span>
<span class="sd">    """</span>

    <span class="n">attributes</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span>
<span class="w">    </span><span class="sd">"""Attributes associated with the task run for this case.</span>

<span class="sd">    These can be set by calling `pydantic_evals.dataset.set_eval_attribute` in any code executed</span>
<span class="sd">    during the evaluation task."""</span>
    <span class="n">metrics</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">int</span> <span class="o">|</span> <span class="nb">float</span><span class="p">]</span>
<span class="w">    </span><span class="sd">"""Metrics associated with the task run for this case.</span>

<span class="sd">    These can be set by calling `pydantic_evals.dataset.increment_eval_metric` in any code executed</span>
<span class="sd">    during the evaluation task."""</span>

    <span class="nd">@property</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">span_tree</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">SpanTree</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get the `SpanTree` for this task execution.</span>

<span class="sd">        The span tree is a graph where each node corresponds to an OpenTelemetry span recorded during the task</span>
<span class="sd">        execution, including timing information and any custom spans created during execution.</span>

<span class="sd">        Returns:</span>
<span class="sd">            The span tree for the task execution.</span>

<span class="sd">        Raises:</span>
<span class="sd">            SpanTreeRecordingError: If spans were not captured during execution of the task, e.g. due to not having</span>
<span class="sd">                the necessary dependencies installed.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_span_tree</span><span class="p">,</span> <span class="n">SpanTreeRecordingError</span><span class="p">):</span>
            <span class="c1"># In this case, there was a reason we couldn't record the SpanTree. We raise that now</span>
            <span class="k">raise</span> <span class="bp">self</span><span class="o">.</span><span class="n">_span_tree</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_span_tree</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-attribute">



<h4 id="pydantic_evals.evaluators.EvaluatorContext.name" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">name</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_10"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_10 > code"></button><code><span class="n">name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The name of the case.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_evals.evaluators.EvaluatorContext.inputs" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">inputs</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_11"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_11 > code"></button><code><span class="n">inputs</span><span class="p">:</span> <span class="n"><span title="pydantic_evals.evaluators.context.InputsT">InputsT</span></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The inputs provided to the task for this case.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_evals.evaluators.EvaluatorContext.metadata" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">metadata</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_12"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_12 > code"></button><code><span class="n">metadata</span><span class="p">:</span> <span class="n"><span title="pydantic_evals.evaluators.context.MetadataT">MetadataT</span></span> <span class="o">|</span> <span class="kc">None</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Metadata associated with the case, if provided. May be None if no metadata was specified.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_evals.evaluators.EvaluatorContext.expected_output" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">expected_output</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_13"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_13 > code"></button><code><span class="n">expected_output</span><span class="p">:</span> <span class="n"><span title="pydantic_evals.evaluators.context.OutputT">OutputT</span></span> <span class="o">|</span> <span class="kc">None</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The expected output for the case, if provided. May be None if no expected output was specified.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_evals.evaluators.EvaluatorContext.output" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">output</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_14"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_14 > code"></button><code><span class="n">output</span><span class="p">:</span> <span class="n"><span title="pydantic_evals.evaluators.context.OutputT">OutputT</span></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The actual output produced by the task for this case.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_evals.evaluators.EvaluatorContext.duration" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">duration</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_15"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_15 > code"></button><code><span class="n">duration</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#float">float</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The duration of the task run for this case.</p>
    </div>

</div>










<div class="doc doc-object doc-attribute">



<h4 id="pydantic_evals.evaluators.EvaluatorContext.attributes" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">attributes</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_16"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_16 > code"></button><code><span class="n">attributes</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict">dict</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a></span><span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Attributes associated with the task run for this case.</p>
<p>These can be set by calling <code>pydantic_evals.dataset.set_eval_attribute</code> in any code executed
during the evaluation task.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_evals.evaluators.EvaluatorContext.metrics" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">metrics</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_17"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_17 > code"></button><code><span class="n">metrics</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#dict">dict</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#int">int</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#float">float</a></span><span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Metrics associated with the task run for this case.</p>
<p>These can be set by calling <code>pydantic_evals.dataset.increment_eval_metric</code> in any code executed
during the evaluation task.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_evals.evaluators.EvaluatorContext.span_tree" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">span_tree</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-property"><code>property</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_18"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_18 > code"></button><code><span class="n">span_tree</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.otel.span_tree.SpanTree" href="../otel/#pydantic_evals.otel.SpanTree">SpanTree</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Get the <code>SpanTree</code> for this task execution.</p>
<p>The span tree is a graph where each node corresponds to an OpenTelemetry span recorded during the task
execution, including timing information and any custom spans created during execution.</p>


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
                  <code><a class="autorefs autorefs-internal" title="pydantic_evals.otel.span_tree.SpanTree" href="../otel/#pydantic_evals.otel.SpanTree">SpanTree</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The span tree for the task execution.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table></div></div>


<p><span class="doc-section-title">Raises:</span></p>
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
                  <code><span title="pydantic_evals.otel._errors.SpanTreeRecordingError">SpanTreeRecordingError</span></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>If spans were not captured during execution of the task, e.g. due to not having
the necessary dependencies installed.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table></div></div>
    </div>

</div>




  </div>

    </div>

</div>






<div class="doc doc-object doc-class">



<h3 id="pydantic_evals.evaluators.EvaluationReason" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">EvaluationReason</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span>

</h3>


    <div class="doc doc-contents ">


        <p>The result of running an evaluator with an optional explanation.</p>
<p>Contains a scalar value and an optional "reason" explaining the value.</p>


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
                <code>value</code>
            </td>
            <td>
                  <code><span title="pydantic_evals.evaluators.evaluator.EvaluationScalar">EvaluationScalar</span></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The scalar result of the evaluation (boolean, integer, float, or string).</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>reason</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>An optional explanation of the evaluation result.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
      </tbody>
    </table></div></div>






              <details class="quote">
                <summary>Source code in <code>pydantic_evals/pydantic_evals/evaluators/evaluator.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">36</span>
<span class="normal">37</span>
<span class="normal">38</span>
<span class="normal">39</span>
<span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span>
<span class="normal">43</span>
<span class="normal">44</span>
<span class="normal">45</span>
<span class="normal">46</span>
<span class="normal">47</span>
<span class="normal">48</span></pre></div></td><td class="code"><div><pre id="__code_19"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_19 > code"></button><code><span class="nd">@dataclass</span>
<span class="k">class</span><span class="w"> </span><span class="nc">EvaluationReason</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""The result of running an evaluator with an optional explanation.</span>

<span class="sd">    Contains a scalar value and an optional "reason" explaining the value.</span>

<span class="sd">    Args:</span>
<span class="sd">        value: The scalar result of the evaluation (boolean, integer, float, or string).</span>
<span class="sd">        reason: An optional explanation of the evaluation result.</span>
<span class="sd">    """</span>

    <span class="n">value</span><span class="p">:</span> <span class="n">EvaluationScalar</span>
    <span class="n">reason</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">





  </div>

    </div>

</div>






<div class="doc doc-object doc-class">



<h3 id="pydantic_evals.evaluators.EvaluationResult" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">EvaluationResult</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span>

</h3>


    <div class="doc doc-contents ">
            <p class="doc doc-class-bases">
              Bases: <code><a class="autorefs autorefs-external" title="typing.Generic" href="https://docs.python.org/3/library/typing.html#typing.Generic">Generic</a>[<span title="pydantic_evals.evaluators.evaluator.EvaluationScalarT">EvaluationScalarT</span>]</code></p>


        <p>The details of an individual evaluation result.</p>
<p>Contains the name, value, reason, and source evaluator for a single evaluation.</p>


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
                <code>name</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The name of the evaluation.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>value</code>
            </td>
            <td>
                  <code><span title="pydantic_evals.evaluators.evaluator.EvaluationScalarT">EvaluationScalarT</span></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The scalar result of the evaluation.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>reason</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>An optional explanation of the evaluation result.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>source</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_evals.evaluators.evaluator.Evaluator" href="#pydantic_evals.evaluators.Evaluator">Evaluator</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The evaluator that produced this result.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
      </tbody>
    </table></div></div>






              <details class="quote">
                <summary>Source code in <code>pydantic_evals/pydantic_evals/evaluators/evaluator.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">62</span>
<span class="normal">63</span>
<span class="normal">64</span>
<span class="normal">65</span>
<span class="normal">66</span>
<span class="normal">67</span>
<span class="normal">68</span>
<span class="normal">69</span>
<span class="normal">70</span>
<span class="normal">71</span>
<span class="normal">72</span>
<span class="normal">73</span>
<span class="normal">74</span>
<span class="normal">75</span>
<span class="normal">76</span>
<span class="normal">77</span>
<span class="normal">78</span>
<span class="normal">79</span>
<span class="normal">80</span>
<span class="normal">81</span>
<span class="normal">82</span>
<span class="normal">83</span>
<span class="normal">84</span>
<span class="normal">85</span>
<span class="normal">86</span>
<span class="normal">87</span>
<span class="normal">88</span>
<span class="normal">89</span>
<span class="normal">90</span>
<span class="normal">91</span>
<span class="normal">92</span>
<span class="normal">93</span>
<span class="normal">94</span>
<span class="normal">95</span>
<span class="normal">96</span>
<span class="normal">97</span></pre></div></td><td class="code"><div><pre id="__code_20"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_20 > code"></button><code><span class="nd">@dataclass</span>
<span class="k">class</span><span class="w"> </span><span class="nc">EvaluationResult</span><span class="p">(</span><span class="n">Generic</span><span class="p">[</span><span class="n">EvaluationScalarT</span><span class="p">]):</span>
<span class="w">    </span><span class="sd">"""The details of an individual evaluation result.</span>

<span class="sd">    Contains the name, value, reason, and source evaluator for a single evaluation.</span>

<span class="sd">    Args:</span>
<span class="sd">        name: The name of the evaluation.</span>
<span class="sd">        value: The scalar result of the evaluation.</span>
<span class="sd">        reason: An optional explanation of the evaluation result.</span>
<span class="sd">        source: The evaluator that produced this result.</span>
<span class="sd">    """</span>

    <span class="n">name</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">value</span><span class="p">:</span> <span class="n">EvaluationScalarT</span>
    <span class="n">reason</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span>
    <span class="n">source</span><span class="p">:</span> <span class="n">Evaluator</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">downcast</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">value_types</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n">T</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">EvaluationResult</span><span class="p">[</span><span class="n">T</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Attempt to downcast this result to a more specific type.</span>

<span class="sd">        Args:</span>
<span class="sd">            *value_types: The types to check the value against.</span>

<span class="sd">        Returns:</span>
<span class="sd">            A downcast version of this result if the value is an instance of one of the given types,</span>
<span class="sd">            otherwise None.</span>
<span class="sd">        """</span>
        <span class="c1"># Check if value matches any of the target types, handling bool as a special case</span>
        <span class="k">for</span> <span class="n">value_type</span> <span class="ow">in</span> <span class="n">value_types</span><span class="p">:</span>
            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">value</span><span class="p">,</span> <span class="n">value_type</span><span class="p">):</span>
                <span class="c1"># Only match bool with explicit bool type</span>
                <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">value</span><span class="p">,</span> <span class="nb">bool</span><span class="p">)</span> <span class="ow">and</span> <span class="n">value_type</span> <span class="ow">is</span> <span class="ow">not</span> <span class="nb">bool</span><span class="p">:</span>
                    <span class="k">continue</span>
                <span class="k">return</span> <span class="n">cast</span><span class="p">(</span><span class="n">EvaluationResult</span><span class="p">[</span><span class="n">T</span><span class="p">],</span> <span class="bp">self</span><span class="p">)</span>
        <span class="k">return</span> <span class="kc">None</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-function">


<h4 id="pydantic_evals.evaluators.EvaluationResult.downcast" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">downcast</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_21"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_21 > code"></button><code><span class="nf">downcast</span><span class="p">(</span>
    <span class="o">*</span><span class="n">value_types</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type">type</a></span><span class="p">[</span><span class="n"><span title="pydantic_evals.evaluators.evaluator.T">T</span></span><span class="p">],</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.evaluators.evaluator.EvaluationResult" href="#pydantic_evals.evaluators.EvaluationResult">EvaluationResult</a></span><span class="p">[</span><span class="n"><span title="pydantic_evals.evaluators.evaluator.T">T</span></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Attempt to downcast this result to a more specific type.</p>


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
                <code>*value_types</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#type">type</a>[<span title="pydantic_evals.evaluators.evaluator.T">T</span>]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The types to check the value against.</p>
              </div>
            </td>
            <td>
                  <code>()</code>
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
                  <code><a class="autorefs autorefs-internal" title="pydantic_evals.evaluators.evaluator.EvaluationResult" href="#pydantic_evals.evaluators.EvaluationResult">EvaluationResult</a>[<span title="pydantic_evals.evaluators.evaluator.T">T</span>] | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>A downcast version of this result if the value is an instance of one of the given types,</p>
              </div>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_evals.evaluators.evaluator.EvaluationResult" href="#pydantic_evals.evaluators.EvaluationResult">EvaluationResult</a>[<span title="pydantic_evals.evaluators.evaluator.T">T</span>] | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>otherwise None.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_evals/pydantic_evals/evaluators/evaluator.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">80</span>
<span class="normal">81</span>
<span class="normal">82</span>
<span class="normal">83</span>
<span class="normal">84</span>
<span class="normal">85</span>
<span class="normal">86</span>
<span class="normal">87</span>
<span class="normal">88</span>
<span class="normal">89</span>
<span class="normal">90</span>
<span class="normal">91</span>
<span class="normal">92</span>
<span class="normal">93</span>
<span class="normal">94</span>
<span class="normal">95</span>
<span class="normal">96</span>
<span class="normal">97</span></pre></div></td><td class="code"><div><pre id="__code_22"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_22 > code"></button><code><span class="k">def</span><span class="w"> </span><span class="nf">downcast</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">value_types</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n">T</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">EvaluationResult</span><span class="p">[</span><span class="n">T</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Attempt to downcast this result to a more specific type.</span>

<span class="sd">    Args:</span>
<span class="sd">        *value_types: The types to check the value against.</span>

<span class="sd">    Returns:</span>
<span class="sd">        A downcast version of this result if the value is an instance of one of the given types,</span>
<span class="sd">        otherwise None.</span>
<span class="sd">    """</span>
    <span class="c1"># Check if value matches any of the target types, handling bool as a special case</span>
    <span class="k">for</span> <span class="n">value_type</span> <span class="ow">in</span> <span class="n">value_types</span><span class="p">:</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">value</span><span class="p">,</span> <span class="n">value_type</span><span class="p">):</span>
            <span class="c1"># Only match bool with explicit bool type</span>
            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">value</span><span class="p">,</span> <span class="nb">bool</span><span class="p">)</span> <span class="ow">and</span> <span class="n">value_type</span> <span class="ow">is</span> <span class="ow">not</span> <span class="nb">bool</span><span class="p">:</span>
                <span class="k">continue</span>
            <span class="k">return</span> <span class="n">cast</span><span class="p">(</span><span class="n">EvaluationResult</span><span class="p">[</span><span class="n">T</span><span class="p">],</span> <span class="bp">self</span><span class="p">)</span>
    <span class="k">return</span> <span class="kc">None</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>




  </div>

    </div>

</div>






<div class="doc doc-object doc-class">



<h3 id="pydantic_evals.evaluators.Evaluator" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">Evaluator</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span>

</h3>


    <div class="doc doc-contents ">
            <p class="doc doc-class-bases">
              Bases: <code><a class="autorefs autorefs-external" title="typing.Generic" href="https://docs.python.org/3/library/typing.html#typing.Generic">Generic</a>[<span title="pydantic_evals.evaluators.evaluator.InputsT">InputsT</span>, <span title="pydantic_evals.evaluators.evaluator.OutputT">OutputT</span>, <span title="pydantic_evals.evaluators.evaluator.MetadataT">MetadataT</span>]</code></p>


        <p>Base class for all evaluators.</p>
<p>Evaluators can assess the performance of a task in a variety of ways, as a function of the EvaluatorContext.</p>
<p>Subclasses must implement the <code>evaluate</code> method. Note it can be defined with either <code>def</code> or <code>async def</code>.</p>
<p>Example:
</p><div class="language-python highlight"><pre id="__code_23"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_23 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">dataclasses</span><span class="w"> </span><span class="kn">import</span> <span class="n">dataclass</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_evals.evaluators</span><span class="w"> </span><span class="kn">import</span> <span class="n">Evaluator</span><span class="p">,</span> <span class="n">EvaluatorContext</span>


<span class="nd">@dataclass</span>
<span class="k">class</span><span class="w"> </span><span class="nc">ExactMatch</span><span class="p">(</span><span class="n">Evaluator</span><span class="p">):</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">evaluate</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ctx</span><span class="p">:</span> <span class="n">EvaluatorContext</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">ctx</span><span class="o">.</span><span class="n">output</span> <span class="o">==</span> <span class="n">ctx</span><span class="o">.</span><span class="n">expected_output</span>
</code></pre></div><p></p>






              <details class="quote">
                <summary>Source code in <code>pydantic_evals/pydantic_evals/evaluators/evaluator.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">124</span>
<span class="normal">125</span>
<span class="normal">126</span>
<span class="normal">127</span>
<span class="normal">128</span>
<span class="normal">129</span>
<span class="normal">130</span>
<span class="normal">131</span>
<span class="normal">132</span>
<span class="normal">133</span>
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
<span class="normal">195</span>
<span class="normal">196</span>
<span class="normal">197</span>
<span class="normal">198</span>
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
<span class="normal">221</span>
<span class="normal">222</span>
<span class="normal">223</span>
<span class="normal">224</span>
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
<span class="normal">245</span></pre></div></td><td class="code"><div><pre id="__code_24"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_24 > code"></button><code tabindex="0"><span class="nd">@dataclass</span>
<span class="k">class</span><span class="w"> </span><span class="nc">Evaluator</span><span class="p">(</span><span class="n">Generic</span><span class="p">[</span><span class="n">InputsT</span><span class="p">,</span> <span class="n">OutputT</span><span class="p">,</span> <span class="n">MetadataT</span><span class="p">],</span> <span class="n">metaclass</span><span class="o">=</span><span class="n">_StrictABCMeta</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Base class for all evaluators.</span>

<span class="sd">    Evaluators can assess the performance of a task in a variety of ways, as a function of the EvaluatorContext.</span>

<span class="sd">    Subclasses must implement the `evaluate` method. Note it can be defined with either `def` or `async def`.</span>

<span class="sd">    Example:</span>
<span class="sd">    ```python</span>
<span class="sd">    from dataclasses import dataclass</span>

<span class="sd">    from pydantic_evals.evaluators import Evaluator, EvaluatorContext</span>


<span class="sd">    @dataclass</span>
<span class="sd">    class ExactMatch(Evaluator):</span>
<span class="sd">        def evaluate(self, ctx: EvaluatorContext) -&gt; bool:</span>
<span class="sd">            return ctx.output == ctx.expected_output</span>
<span class="sd">    ```</span>
<span class="sd">    """</span>

    <span class="n">__pydantic_config__</span> <span class="o">=</span> <span class="n">ConfigDict</span><span class="p">(</span><span class="n">arbitrary_types_allowed</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Return the 'name' of this Evaluator to use during serialization.</span>

<span class="sd">        Returns:</span>
<span class="sd">            The name of the Evaluator, which is typically the class name.</span>
<span class="sd">        """</span>
        <span class="c1"># Note: if we wanted to prefer snake_case, we could use:</span>
        <span class="c1"># from pydantic.alias_generators import to_snake</span>
        <span class="c1"># return to_snake(cls.__name__)</span>
        <span class="k">return</span> <span class="bp">cls</span><span class="o">.</span><span class="vm">__name__</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">evaluate</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">ctx</span><span class="p">:</span> <span class="n">EvaluatorContext</span><span class="p">[</span><span class="n">InputsT</span><span class="p">,</span> <span class="n">OutputT</span><span class="p">,</span> <span class="n">MetadataT</span><span class="p">]</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">EvaluatorOutput</span> <span class="o">|</span> <span class="n">Awaitable</span><span class="p">[</span><span class="n">EvaluatorOutput</span><span class="p">]:</span>  <span class="c1"># pragma: no cover</span>
<span class="w">        </span><span class="sd">"""Evaluate the task output in the given context.</span>

<span class="sd">        This is the main evaluation method that subclasses must implement. It can be either synchronous</span>
<span class="sd">        or asynchronous, returning either an EvaluatorOutput directly or an Awaitable[EvaluatorOutput].</span>

<span class="sd">        Args:</span>
<span class="sd">            ctx: The context containing the inputs, outputs, and metadata for evaluation.</span>

<span class="sd">        Returns:</span>
<span class="sd">            The evaluation result, which can be a scalar value, an EvaluationReason, or a mapping</span>
<span class="sd">            of evaluation names to either of those. Can be returned either synchronously or as an</span>
<span class="sd">            awaitable for asynchronous evaluation.</span>
<span class="sd">        """</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span><span class="s1">'You must implement `evaluate`.'</span><span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">evaluate_sync</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ctx</span><span class="p">:</span> <span class="n">EvaluatorContext</span><span class="p">[</span><span class="n">InputsT</span><span class="p">,</span> <span class="n">OutputT</span><span class="p">,</span> <span class="n">MetadataT</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">EvaluatorOutput</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run the evaluator synchronously, handling both sync and async implementations.</span>

<span class="sd">        This method ensures synchronous execution by running any async evaluate implementation</span>
<span class="sd">        to completion using run_until_complete.</span>

<span class="sd">        Args:</span>
<span class="sd">            ctx: The context containing the inputs, outputs, and metadata for evaluation.</span>

<span class="sd">        Returns:</span>
<span class="sd">            The evaluation result, which can be a scalar value, an EvaluationReason, or a mapping</span>
<span class="sd">            of evaluation names to either of those.</span>
<span class="sd">        """</span>
        <span class="n">output</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">evaluate</span><span class="p">(</span><span class="n">ctx</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">inspect</span><span class="o">.</span><span class="n">iscoroutine</span><span class="p">(</span><span class="n">output</span><span class="p">):</span>  <span class="c1"># pragma: no cover</span>
            <span class="k">return</span> <span class="n">get_event_loop</span><span class="p">()</span><span class="o">.</span><span class="n">run_until_complete</span><span class="p">(</span><span class="n">output</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">cast</span><span class="p">(</span><span class="n">EvaluatorOutput</span><span class="p">,</span> <span class="n">output</span><span class="p">)</span>

    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">evaluate_async</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ctx</span><span class="p">:</span> <span class="n">EvaluatorContext</span><span class="p">[</span><span class="n">InputsT</span><span class="p">,</span> <span class="n">OutputT</span><span class="p">,</span> <span class="n">MetadataT</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">EvaluatorOutput</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Run the evaluator asynchronously, handling both sync and async implementations.</span>

<span class="sd">        This method ensures asynchronous execution by properly awaiting any async evaluate</span>
<span class="sd">        implementation. For synchronous implementations, it returns the result directly.</span>

<span class="sd">        Args:</span>
<span class="sd">            ctx: The context containing the inputs, outputs, and metadata for evaluation.</span>

<span class="sd">        Returns:</span>
<span class="sd">            The evaluation result, which can be a scalar value, an EvaluationReason, or a mapping</span>
<span class="sd">            of evaluation names to either of those.</span>
<span class="sd">        """</span>
        <span class="c1"># Note: If self.evaluate is synchronous, but you need to prevent this from blocking, override this method with:</span>
        <span class="c1"># return await anyio.to_thread.run_sync(self.evaluate, ctx)</span>
        <span class="n">output</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">evaluate</span><span class="p">(</span><span class="n">ctx</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">inspect</span><span class="o">.</span><span class="n">iscoroutine</span><span class="p">(</span><span class="n">output</span><span class="p">):</span>
            <span class="k">return</span> <span class="k">await</span> <span class="n">output</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">cast</span><span class="p">(</span><span class="n">EvaluatorOutput</span><span class="p">,</span> <span class="n">output</span><span class="p">)</span>

    <span class="nd">@model_serializer</span><span class="p">(</span><span class="n">mode</span><span class="o">=</span><span class="s1">'plain'</span><span class="p">)</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">serialize</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">info</span><span class="p">:</span> <span class="n">SerializationInfo</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Serialize this Evaluator to a JSON-serializable form.</span>

<span class="sd">        Returns:</span>
<span class="sd">            A JSON-serializable representation of this evaluator as an EvaluatorSpec.</span>
<span class="sd">        """</span>
        <span class="n">raw_arguments</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="k">for</span> <span class="n">field</span> <span class="ow">in</span> <span class="n">fields</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
            <span class="n">value</span> <span class="o">=</span> <span class="nb">getattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">field</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
            <span class="c1"># always exclude defaults:</span>
            <span class="k">if</span> <span class="n">field</span><span class="o">.</span><span class="n">default</span> <span class="ow">is</span> <span class="ow">not</span> <span class="n">MISSING</span><span class="p">:</span>
                <span class="k">if</span> <span class="n">value</span> <span class="o">==</span> <span class="n">field</span><span class="o">.</span><span class="n">default</span><span class="p">:</span>
                    <span class="k">continue</span>
            <span class="k">if</span> <span class="n">field</span><span class="o">.</span><span class="n">default_factory</span> <span class="ow">is</span> <span class="ow">not</span> <span class="n">MISSING</span><span class="p">:</span>
                <span class="k">if</span> <span class="n">value</span> <span class="o">==</span> <span class="n">field</span><span class="o">.</span><span class="n">default_factory</span><span class="p">():</span>
                    <span class="k">continue</span>
            <span class="n">raw_arguments</span><span class="p">[</span><span class="n">field</span><span class="o">.</span><span class="n">name</span><span class="p">]</span> <span class="o">=</span> <span class="n">value</span>

        <span class="n">arguments</span><span class="p">:</span> <span class="kc">None</span> <span class="o">|</span> <span class="nb">tuple</span><span class="p">[</span><span class="n">Any</span><span class="p">,]</span> <span class="o">|</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span>
        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">raw_arguments</span><span class="p">)</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
            <span class="n">arguments</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="k">elif</span> <span class="nb">len</span><span class="p">(</span><span class="n">raw_arguments</span><span class="p">)</span> <span class="o">==</span> <span class="mi">1</span><span class="p">:</span>
            <span class="n">arguments</span> <span class="o">=</span> <span class="p">(</span><span class="nb">next</span><span class="p">(</span><span class="nb">iter</span><span class="p">(</span><span class="n">raw_arguments</span><span class="o">.</span><span class="n">values</span><span class="p">())),)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">arguments</span> <span class="o">=</span> <span class="n">raw_arguments</span>
        <span class="k">return</span> <span class="n">to_jsonable_python</span><span class="p">(</span><span class="n">EvaluatorSpec</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="p">(),</span> <span class="n">arguments</span><span class="o">=</span><span class="n">arguments</span><span class="p">),</span> <span class="n">context</span><span class="o">=</span><span class="n">info</span><span class="o">.</span><span class="n">context</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-function">


<h4 id="pydantic_evals.evaluators.Evaluator.name" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">name</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-classmethod"><code>classmethod</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_25"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_25 > code"></button><code><span class="nf">name</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Return the 'name' of this Evaluator to use during serialization.</p>


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
                <p>The name of the Evaluator, which is typically the class name.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_evals/pydantic_evals/evaluators/evaluator.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">148</span>
<span class="normal">149</span>
<span class="normal">150</span>
<span class="normal">151</span>
<span class="normal">152</span>
<span class="normal">153</span>
<span class="normal">154</span>
<span class="normal">155</span>
<span class="normal">156</span>
<span class="normal">157</span>
<span class="normal">158</span></pre></div></td><td class="code"><div><pre id="__code_26"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_26 > code"></button><code><span class="nd">@classmethod</span>
<span class="k">def</span><span class="w"> </span><span class="nf">name</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Return the 'name' of this Evaluator to use during serialization.</span>

<span class="sd">    Returns:</span>
<span class="sd">        The name of the Evaluator, which is typically the class name.</span>
<span class="sd">    """</span>
    <span class="c1"># Note: if we wanted to prefer snake_case, we could use:</span>
    <span class="c1"># from pydantic.alias_generators import to_snake</span>
    <span class="c1"># return to_snake(cls.__name__)</span>
    <span class="k">return</span> <span class="bp">cls</span><span class="o">.</span><span class="vm">__name__</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_evals.evaluators.Evaluator.evaluate" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">evaluate</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-abstractmethod"><code>abstractmethod</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_27"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_27 > code"></button><code><span class="nf">evaluate</span><span class="p">(</span>
    <span class="n">ctx</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.evaluators.context.EvaluatorContext" href="#pydantic_evals.evaluators.EvaluatorContext">EvaluatorContext</a></span><span class="p">[</span><span class="n"><span title="pydantic_evals.evaluators.evaluator.InputsT">InputsT</span></span><span class="p">,</span> <span class="n"><span title="pydantic_evals.evaluators.evaluator.OutputT">OutputT</span></span><span class="p">,</span> <span class="n"><span title="pydantic_evals.evaluators.evaluator.MetadataT">MetadataT</span></span><span class="p">],</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.evaluators.evaluator.EvaluatorOutput" href="#pydantic_evals.evaluators.EvaluatorOutput">EvaluatorOutput</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" title="collections.abc.Awaitable" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Awaitable">Awaitable</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.evaluators.evaluator.EvaluatorOutput" href="#pydantic_evals.evaluators.EvaluatorOutput">EvaluatorOutput</a></span><span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Evaluate the task output in the given context.</p>
<p>This is the main evaluation method that subclasses must implement. It can be either synchronous
or asynchronous, returning either an EvaluatorOutput directly or an Awaitable[EvaluatorOutput].</p>


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
                <code>ctx</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_evals.evaluators.context.EvaluatorContext" href="#pydantic_evals.evaluators.EvaluatorContext">EvaluatorContext</a>[<span title="pydantic_evals.evaluators.evaluator.InputsT">InputsT</span>, <span title="pydantic_evals.evaluators.evaluator.OutputT">OutputT</span>, <span title="pydantic_evals.evaluators.evaluator.MetadataT">MetadataT</span>]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The context containing the inputs, outputs, and metadata for evaluation.</p>
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
                  <code><a class="autorefs autorefs-internal" title="pydantic_evals.evaluators.evaluator.EvaluatorOutput" href="#pydantic_evals.evaluators.EvaluatorOutput">EvaluatorOutput</a> | <a class="autorefs autorefs-external" title="collections.abc.Awaitable" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Awaitable">Awaitable</a>[<a class="autorefs autorefs-internal" title="pydantic_evals.evaluators.evaluator.EvaluatorOutput" href="#pydantic_evals.evaluators.EvaluatorOutput">EvaluatorOutput</a>]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The evaluation result, which can be a scalar value, an EvaluationReason, or a mapping</p>
              </div>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_evals.evaluators.evaluator.EvaluatorOutput" href="#pydantic_evals.evaluators.EvaluatorOutput">EvaluatorOutput</a> | <a class="autorefs autorefs-external" title="collections.abc.Awaitable" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Awaitable">Awaitable</a>[<a class="autorefs autorefs-internal" title="pydantic_evals.evaluators.evaluator.EvaluatorOutput" href="#pydantic_evals.evaluators.EvaluatorOutput">EvaluatorOutput</a>]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>of evaluation names to either of those. Can be returned either synchronously or as an</p>
              </div>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_evals.evaluators.evaluator.EvaluatorOutput" href="#pydantic_evals.evaluators.EvaluatorOutput">EvaluatorOutput</a> | <a class="autorefs autorefs-external" title="collections.abc.Awaitable" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Awaitable">Awaitable</a>[<a class="autorefs autorefs-internal" title="pydantic_evals.evaluators.evaluator.EvaluatorOutput" href="#pydantic_evals.evaluators.EvaluatorOutput">EvaluatorOutput</a>]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>awaitable for asynchronous evaluation.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_evals/pydantic_evals/evaluators/evaluator.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">160</span>
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
<span class="normal">177</span></pre></div></td><td class="code"><div><pre id="__code_28"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_28 > code"></button><code><span class="nd">@abstractmethod</span>
<span class="k">def</span><span class="w"> </span><span class="nf">evaluate</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span> <span class="n">ctx</span><span class="p">:</span> <span class="n">EvaluatorContext</span><span class="p">[</span><span class="n">InputsT</span><span class="p">,</span> <span class="n">OutputT</span><span class="p">,</span> <span class="n">MetadataT</span><span class="p">]</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">EvaluatorOutput</span> <span class="o">|</span> <span class="n">Awaitable</span><span class="p">[</span><span class="n">EvaluatorOutput</span><span class="p">]:</span>  <span class="c1"># pragma: no cover</span>
<span class="w">    </span><span class="sd">"""Evaluate the task output in the given context.</span>

<span class="sd">    This is the main evaluation method that subclasses must implement. It can be either synchronous</span>
<span class="sd">    or asynchronous, returning either an EvaluatorOutput directly or an Awaitable[EvaluatorOutput].</span>

<span class="sd">    Args:</span>
<span class="sd">        ctx: The context containing the inputs, outputs, and metadata for evaluation.</span>

<span class="sd">    Returns:</span>
<span class="sd">        The evaluation result, which can be a scalar value, an EvaluationReason, or a mapping</span>
<span class="sd">        of evaluation names to either of those. Can be returned either synchronously or as an</span>
<span class="sd">        awaitable for asynchronous evaluation.</span>
<span class="sd">    """</span>
    <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span><span class="s1">'You must implement `evaluate`.'</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_evals.evaluators.Evaluator.evaluate_sync" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">evaluate_sync</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_29"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_29 > code"></button><code><span class="nf">evaluate_sync</span><span class="p">(</span>
    <span class="n">ctx</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.evaluators.context.EvaluatorContext" href="#pydantic_evals.evaluators.EvaluatorContext">EvaluatorContext</a></span><span class="p">[</span><span class="n"><span title="pydantic_evals.evaluators.evaluator.InputsT">InputsT</span></span><span class="p">,</span> <span class="n"><span title="pydantic_evals.evaluators.evaluator.OutputT">OutputT</span></span><span class="p">,</span> <span class="n"><span title="pydantic_evals.evaluators.evaluator.MetadataT">MetadataT</span></span><span class="p">],</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.evaluators.evaluator.EvaluatorOutput" href="#pydantic_evals.evaluators.EvaluatorOutput">EvaluatorOutput</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Run the evaluator synchronously, handling both sync and async implementations.</p>
<p>This method ensures synchronous execution by running any async evaluate implementation
to completion using run_until_complete.</p>


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
                <code>ctx</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_evals.evaluators.context.EvaluatorContext" href="#pydantic_evals.evaluators.EvaluatorContext">EvaluatorContext</a>[<span title="pydantic_evals.evaluators.evaluator.InputsT">InputsT</span>, <span title="pydantic_evals.evaluators.evaluator.OutputT">OutputT</span>, <span title="pydantic_evals.evaluators.evaluator.MetadataT">MetadataT</span>]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The context containing the inputs, outputs, and metadata for evaluation.</p>
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
                  <code><a class="autorefs autorefs-internal" title="pydantic_evals.evaluators.evaluator.EvaluatorOutput" href="#pydantic_evals.evaluators.EvaluatorOutput">EvaluatorOutput</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The evaluation result, which can be a scalar value, an EvaluationReason, or a mapping</p>
              </div>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_evals.evaluators.evaluator.EvaluatorOutput" href="#pydantic_evals.evaluators.EvaluatorOutput">EvaluatorOutput</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>of evaluation names to either of those.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_evals/pydantic_evals/evaluators/evaluator.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">179</span>
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
<span class="normal">195</span>
<span class="normal">196</span></pre></div></td><td class="code"><div><pre id="__code_30"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_30 > code"></button><code><span class="k">def</span><span class="w"> </span><span class="nf">evaluate_sync</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ctx</span><span class="p">:</span> <span class="n">EvaluatorContext</span><span class="p">[</span><span class="n">InputsT</span><span class="p">,</span> <span class="n">OutputT</span><span class="p">,</span> <span class="n">MetadataT</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">EvaluatorOutput</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run the evaluator synchronously, handling both sync and async implementations.</span>

<span class="sd">    This method ensures synchronous execution by running any async evaluate implementation</span>
<span class="sd">    to completion using run_until_complete.</span>

<span class="sd">    Args:</span>
<span class="sd">        ctx: The context containing the inputs, outputs, and metadata for evaluation.</span>

<span class="sd">    Returns:</span>
<span class="sd">        The evaluation result, which can be a scalar value, an EvaluationReason, or a mapping</span>
<span class="sd">        of evaluation names to either of those.</span>
<span class="sd">    """</span>
    <span class="n">output</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">evaluate</span><span class="p">(</span><span class="n">ctx</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">inspect</span><span class="o">.</span><span class="n">iscoroutine</span><span class="p">(</span><span class="n">output</span><span class="p">):</span>  <span class="c1"># pragma: no cover</span>
        <span class="k">return</span> <span class="n">get_event_loop</span><span class="p">()</span><span class="o">.</span><span class="n">run_until_complete</span><span class="p">(</span><span class="n">output</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">cast</span><span class="p">(</span><span class="n">EvaluatorOutput</span><span class="p">,</span> <span class="n">output</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_evals.evaluators.Evaluator.evaluate_async" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">evaluate_async</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-async"><code>async</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_31"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_31 > code"></button><code><span class="nf">evaluate_async</span><span class="p">(</span>
    <span class="n">ctx</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.evaluators.context.EvaluatorContext" href="#pydantic_evals.evaluators.EvaluatorContext">EvaluatorContext</a></span><span class="p">[</span><span class="n"><span title="pydantic_evals.evaluators.evaluator.InputsT">InputsT</span></span><span class="p">,</span> <span class="n"><span title="pydantic_evals.evaluators.evaluator.OutputT">OutputT</span></span><span class="p">,</span> <span class="n"><span title="pydantic_evals.evaluators.evaluator.MetadataT">MetadataT</span></span><span class="p">],</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.evaluators.evaluator.EvaluatorOutput" href="#pydantic_evals.evaluators.EvaluatorOutput">EvaluatorOutput</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Run the evaluator asynchronously, handling both sync and async implementations.</p>
<p>This method ensures asynchronous execution by properly awaiting any async evaluate
implementation. For synchronous implementations, it returns the result directly.</p>


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
                <code>ctx</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_evals.evaluators.context.EvaluatorContext" href="#pydantic_evals.evaluators.EvaluatorContext">EvaluatorContext</a>[<span title="pydantic_evals.evaluators.evaluator.InputsT">InputsT</span>, <span title="pydantic_evals.evaluators.evaluator.OutputT">OutputT</span>, <span title="pydantic_evals.evaluators.evaluator.MetadataT">MetadataT</span>]</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The context containing the inputs, outputs, and metadata for evaluation.</p>
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
                  <code><a class="autorefs autorefs-internal" title="pydantic_evals.evaluators.evaluator.EvaluatorOutput" href="#pydantic_evals.evaluators.EvaluatorOutput">EvaluatorOutput</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The evaluation result, which can be a scalar value, an EvaluationReason, or a mapping</p>
              </div>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                  <code><a class="autorefs autorefs-internal" title="pydantic_evals.evaluators.evaluator.EvaluatorOutput" href="#pydantic_evals.evaluators.EvaluatorOutput">EvaluatorOutput</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>of evaluation names to either of those.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_evals/pydantic_evals/evaluators/evaluator.py</code></summary>
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
<span class="normal">217</span></pre></div></td><td class="code"><div><pre id="__code_32"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_32 > code"></button><code tabindex="0"><span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">evaluate_async</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ctx</span><span class="p">:</span> <span class="n">EvaluatorContext</span><span class="p">[</span><span class="n">InputsT</span><span class="p">,</span> <span class="n">OutputT</span><span class="p">,</span> <span class="n">MetadataT</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">EvaluatorOutput</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Run the evaluator asynchronously, handling both sync and async implementations.</span>

<span class="sd">    This method ensures asynchronous execution by properly awaiting any async evaluate</span>
<span class="sd">    implementation. For synchronous implementations, it returns the result directly.</span>

<span class="sd">    Args:</span>
<span class="sd">        ctx: The context containing the inputs, outputs, and metadata for evaluation.</span>

<span class="sd">    Returns:</span>
<span class="sd">        The evaluation result, which can be a scalar value, an EvaluationReason, or a mapping</span>
<span class="sd">        of evaluation names to either of those.</span>
<span class="sd">    """</span>
    <span class="c1"># Note: If self.evaluate is synchronous, but you need to prevent this from blocking, override this method with:</span>
    <span class="c1"># return await anyio.to_thread.run_sync(self.evaluate, ctx)</span>
    <span class="n">output</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">evaluate</span><span class="p">(</span><span class="n">ctx</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">inspect</span><span class="o">.</span><span class="n">iscoroutine</span><span class="p">(</span><span class="n">output</span><span class="p">):</span>
        <span class="k">return</span> <span class="k">await</span> <span class="n">output</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">cast</span><span class="p">(</span><span class="n">EvaluatorOutput</span><span class="p">,</span> <span class="n">output</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_evals.evaluators.Evaluator.serialize" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">serialize</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_33"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_33 > code"></button><code><span class="nf">serialize</span><span class="p">(</span><span class="n">info</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="pydantic_core.core_schema.SerializationInfo" href="https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.SerializationInfo">SerializationInfo</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Serialize this Evaluator to a JSON-serializable form.</p>


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
                  <code><a class="autorefs autorefs-external" title="typing.Any" href="https://docs.python.org/3/library/typing.html#typing.Any">Any</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>A JSON-serializable representation of this evaluator as an EvaluatorSpec.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_evals/pydantic_evals/evaluators/evaluator.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">219</span>
<span class="normal">220</span>
<span class="normal">221</span>
<span class="normal">222</span>
<span class="normal">223</span>
<span class="normal">224</span>
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
<span class="normal">245</span></pre></div></td><td class="code"><div><pre id="__code_34"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_34 > code"></button><code><span class="nd">@model_serializer</span><span class="p">(</span><span class="n">mode</span><span class="o">=</span><span class="s1">'plain'</span><span class="p">)</span>
<span class="k">def</span><span class="w"> </span><span class="nf">serialize</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">info</span><span class="p">:</span> <span class="n">SerializationInfo</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Serialize this Evaluator to a JSON-serializable form.</span>

<span class="sd">    Returns:</span>
<span class="sd">        A JSON-serializable representation of this evaluator as an EvaluatorSpec.</span>
<span class="sd">    """</span>
    <span class="n">raw_arguments</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="p">{}</span>
    <span class="k">for</span> <span class="n">field</span> <span class="ow">in</span> <span class="n">fields</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="n">value</span> <span class="o">=</span> <span class="nb">getattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">field</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
        <span class="c1"># always exclude defaults:</span>
        <span class="k">if</span> <span class="n">field</span><span class="o">.</span><span class="n">default</span> <span class="ow">is</span> <span class="ow">not</span> <span class="n">MISSING</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">value</span> <span class="o">==</span> <span class="n">field</span><span class="o">.</span><span class="n">default</span><span class="p">:</span>
                <span class="k">continue</span>
        <span class="k">if</span> <span class="n">field</span><span class="o">.</span><span class="n">default_factory</span> <span class="ow">is</span> <span class="ow">not</span> <span class="n">MISSING</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">value</span> <span class="o">==</span> <span class="n">field</span><span class="o">.</span><span class="n">default_factory</span><span class="p">():</span>
                <span class="k">continue</span>
        <span class="n">raw_arguments</span><span class="p">[</span><span class="n">field</span><span class="o">.</span><span class="n">name</span><span class="p">]</span> <span class="o">=</span> <span class="n">value</span>

    <span class="n">arguments</span><span class="p">:</span> <span class="kc">None</span> <span class="o">|</span> <span class="nb">tuple</span><span class="p">[</span><span class="n">Any</span><span class="p">,]</span> <span class="o">|</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span>
    <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">raw_arguments</span><span class="p">)</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
        <span class="n">arguments</span> <span class="o">=</span> <span class="kc">None</span>
    <span class="k">elif</span> <span class="nb">len</span><span class="p">(</span><span class="n">raw_arguments</span><span class="p">)</span> <span class="o">==</span> <span class="mi">1</span><span class="p">:</span>
        <span class="n">arguments</span> <span class="o">=</span> <span class="p">(</span><span class="nb">next</span><span class="p">(</span><span class="nb">iter</span><span class="p">(</span><span class="n">raw_arguments</span><span class="o">.</span><span class="n">values</span><span class="p">())),)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">arguments</span> <span class="o">=</span> <span class="n">raw_arguments</span>
    <span class="k">return</span> <span class="n">to_jsonable_python</span><span class="p">(</span><span class="n">EvaluatorSpec</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="p">(),</span> <span class="n">arguments</span><span class="o">=</span><span class="n">arguments</span><span class="p">),</span> <span class="n">context</span><span class="o">=</span><span class="n">info</span><span class="o">.</span><span class="n">context</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>




  </div>

    </div>

</div>






<div class="doc doc-object doc-attribute">



<h3 id="pydantic_evals.evaluators.EvaluatorOutput" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">EvaluatorOutput</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
  </span>

</h3>
<div class="language-python doc-signature highlight"><pre id="__code_35"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_35 > code"></button><code><span class="n">EvaluatorOutput</span> <span class="o">=</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Union" href="https://docs.python.org/3/library/typing.html#typing.Union">Union</a></span><span class="p">[</span>
    <span class="n"><span title="pydantic_evals.evaluators.evaluator.EvaluationScalar">EvaluationScalar</span></span><span class="p">,</span>
    <span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.evaluators.evaluator.EvaluationReason" href="#pydantic_evals.evaluators.EvaluationReason">EvaluationReason</a></span><span class="p">,</span>
    <span class="n"><a class="autorefs autorefs-external" title="collections.abc.Mapping" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping">Mapping</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Union" href="https://docs.python.org/3/library/typing.html#typing.Union">Union</a></span><span class="p">[</span><span class="n"><span title="pydantic_evals.evaluators.evaluator.EvaluationScalar">EvaluationScalar</span></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_evals.evaluators.evaluator.EvaluationReason" href="#pydantic_evals.evaluators.EvaluationReason">EvaluationReason</a></span><span class="p">]],</span>
<span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Type for the output of an evaluator, which can be a scalar, an EvaluationReason, or a mapping of names to either.</p>
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